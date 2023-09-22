module.exports = {
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    content: [
        '../**/templates/*.html',
        '../**/templates/**/*.html',
        './templates/**/*.html',
        './node_modules/flowbite/**/*.js'
        ],
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [ 
        require('tw-elements/dist/plugin'), 
        require('autoprefixer')
    ], 
}