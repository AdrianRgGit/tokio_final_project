/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        '../../**/*.py'
    ],
    theme: {
        colors: {
          "black-1": "#010101",
          "white-1": "#E4E4E7",
          "gray-1": "#3D3B40",
          "gray-2": "#B4B4B3",
          "cream-1": "#EBE4D1",
          "red-1": "#FF6252",
          "orange-1": "#E55604",
          "green-1": "#2AC670",
          "blue-1": "#26577C",
          "yellow-1": "#F6D776",
          "purple-1": "#7360DF"
        },

        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
