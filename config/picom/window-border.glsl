#version 330

in vec2 texcoord;
uniform sampler2D tex;
uniform vec2 effective_size;
uniform float corner_radius;

vec4 default_post_processing(vec4 c);

#ifndef BORDER_WIDTH
#define BORDER_WIDTH 1.0
#endif
#ifndef BORDER_ALPHA
#define BORDER_ALPHA 0.55
#endif
#ifndef BORDER_RGB
#define BORDER_RGB vec3(0x8d, 0x91, 0x97) / 255.0
#endif
#ifndef INNER_RADIUS_EXTRA
#define INNER_RADIUS_EXTRA 2.0
#endif
#ifndef LINE_TOLERANCE
#define LINE_TOLERANCE 0.05
#endif

vec4 window_shader() {
	vec2 texsize = textureSize(tex, 0);
	vec4 c = texture2D(tex, texcoord / texsize, 0);
	float inner_radius = corner_radius + INNER_RADIUS_EXTRA;
	vec2 half_size = effective_size / 2.0;
	vec2 q = abs(texcoord - half_size) - (half_size - BORDER_WIDTH - inner_radius);
	float outside_inner = length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - inner_radius;
	if (outside_inner <= 0.0) {
#ifdef BACKGROUND_RGB
		vec3 span = FOREGROUND_RGB - BACKGROUND_RGB;
		float t = clamp(dot(c.rgb - BACKGROUND_RGB, span) / dot(span, span), 0.0, 1.0);
		if (distance(c.rgb, BACKGROUND_RGB + t * span) <= LINE_TOLERANCE) {
			float clear = (1.0 - t) * (1.0 - BACKGROUND_ALPHA);
			c = vec4(c.rgb - BACKGROUND_RGB * clear, 1.0 - clear);
		}
#endif
		return default_post_processing(c);
	}
	float mask = default_post_processing(vec4(1.0)).a;
	return vec4(BORDER_RGB, 1.0) * BORDER_ALPHA * mask;
}
