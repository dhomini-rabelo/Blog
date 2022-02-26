




export const baseHead = {
    group: 'main',
}

export const baseStyles = [
    '/static/styles/_compacts/min/main.min.css',
]

export const scriptsControl = {
    types: [
        'main',
    ],

    scripts: {
        main: [
            ['/static/scripts/features/components/header/hamburguerAnimation.js'],
            ['/static/scripts/features/components/header/inputWidthControl.js'],
            ['/static/scripts/SPA-renders/main/baseMobile.js', true],
            ['/static/scripts/SPA-renders/main/basePC.js', true],
        ]
    }
}