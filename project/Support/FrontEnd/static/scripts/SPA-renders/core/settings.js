export let microsSPA = {

    main : {

        styles: [
            '/static/styles/_compacts/min/main.min.css',
        ],

        scriptsTypes : [
            'main',
        ]

    }


}

export let scriptsSPA = {
    main: [
        ['/static/scripts/features/components/header/hamburguerAnimation.js'],
        ['/static/scripts/features/components/header/inputWidthControl.js'],
        ['/static/scripts/SPA-renders/main/baseMobile.js', true],
        ['/static/scripts/SPA-renders/main/basePC.js', true],
    ]
}