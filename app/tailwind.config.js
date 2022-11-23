/** @type {import('tailwindcss').Config} */
// tailwind.config.js
module.exports = {
	content: [
		"./src/**/*.{js,jsx,ts,tsx}",
	],
	theme: {
		extend: {
			colors: {
				'blacked': '#21252b',
			  },
			fontFamily: {
				'poppins': ['"Poppins"'],
			},
			fontSize: {
				'movie-title': '4rem',
			},
		},
	},
	variants: {},
	plugins: [
		require('tailwind-scrollbar-hide')
		// ...
	  ]
};
