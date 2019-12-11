


require('dotenv').config();
const HtmlWebpackPlugin = require('html-webpack-plugin')
let mix = require('laravel-mix');



mix.webpackConfig({
    resolve: {
        alias: {
            '@module': __dirname + '/app/module',
            '@resource': __dirname + '/resources/assets/js/vue',
        },
    },
    // entry: __dirname + '/public/vue_test.html',
    // output: {
    //     path: __dirname + '/public',
    //     filename: 'index_bundle.html'
    // },
    plugins: [
        new HtmlWebpackPlugin({
            filename: __dirname + '/public/index.html',
            inject:false,
            template: __dirname + '/resources/assets/js/vue/layout/index.ejs'
        })
    ]
});
/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.js('resources/assets/js/vue/app.js', 'public/'+process.env.MIX_VERSION+'/js')
   .sass('resources/assets/sass/app.scss', 'public/'+process.env.MIX_VERSION+'/css');


mix.combine('resources/js/vue_translation/translation.js', 'public/'+process.env.MIX_VERSION+'/js/vue_translation/translation.js');



