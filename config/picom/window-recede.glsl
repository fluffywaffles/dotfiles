#version 330

in vec2 texcoord;
uniform sampler2D tex;
uniform vec2 effective_size;
uniform vec4 tint;

vec4 default_post_processing(vec4 c);

#ifndef BLUR_SCALE
#define BLUR_SCALE 3.0
#endif
#ifndef TOP_SCALE
#define TOP_SCALE 0.88
#endif

const float offsets[3] = float[](0.0, 1.3846153846, 3.2307692308);
const float weights[3] = float[](0.2270270270, 0.3162162162, 0.0702702703);

// picom hands the shader one premultiplied tint of (1 - dim) * opacity, so dividing the colour
// back out by the opacity leaves the dim, which is the rule's signal for how far back to sit.
float away() {
	return tint.a > 0.0 ? clamp(1.0 - tint.r / tint.a, 0.0, 1.0) : 0.0;
}

vec4 tap(vec2 texsize, vec2 at) {
	return texture2D(tex, clamp(at, vec2(0.5), effective_size - 0.5) / texsize, 0);
}

// Where to read for a fragment, if the window were a plane hinged at its bottom edge and
// tilted away: rows bunch toward the top, and each row narrows by its distance.
vec2 tilted(vec2 at, float top) {
	vec2 p = at / effective_size;
	float v = p.y * top / (1.0 - p.y * (1.0 - top));
	float row = top + (1.0 - top) * v;

	return vec2(0.5 + (p.x - 0.5) / row, v) * effective_size;
}

vec4 window_shader() {
	vec2 texsize = textureSize(tex, 0);
	float back = away();
	// Opacity and the rounded corners, taken as a mask so the dim carries no darkening of
	// its own: here it is a position in the animation rather than a colour.
	float mask = default_post_processing(vec4(1.0)).a;

	if (back <= 0.0) {
		return tap(texsize, texcoord) * mask;
	}

	vec2 source = tilted(texcoord, mix(1.0, TOP_SCALE, back));
	float inset = min(source.x, effective_size.x - source.x);
	float edge = smoothstep(0.0, fwidth(source.x), inset);

	if (edge <= 0.0) {
		return vec4(0.0);
	}

	vec4 c = vec4(0.0);

	for (int x = -2; x <= 2; x++) {
		for (int y = -2; y <= 2; y++) {
			vec2 at = source + BLUR_SCALE * back * vec2(sign(x) * offsets[abs(x)], sign(y) * offsets[abs(y)]);
			c += weights[abs(x)] * weights[abs(y)] * tap(texsize, at);
		}
	}

	return c * edge * mask;
}
