Vue.component("step-navigation-step", {
    template: "#step-navigation-step-template",

    props: ["step", "currentstep"],

    computed: {
        indicatorclass() {
            return {
                active: this.step.id == this.currentstep,
                complete: this.currentstep > this.step.id
            };
        }
    }
});

Vue.component("step-navigation", {
    template: "#step-navigation-template",

    props: ["steps", "currentstep"]
});

Vue.component("step", {
    template: "#step-template",

    props: ["step", "stepcount", "currentstep"],

    computed: {
        active() {
            return this.step.id == this.currentstep;
        },

        firststep() {
            return this.currentstep == 1;
        },

        laststep() {
            return this.currentstep == this.stepcount;
        },

        stepWrapperClass() {
            return {
                active: this.active
            };
        }
    },

    methods: {
        nextStep() {
            this.$emit("step-change", this.currentstep + 1);
        },

        lastStep() {
            this.$emit("step-change", this.currentstep - 1);
        }
    }
});

new Vue({
    el: "#app",

    data: {
        currentstep: 1,

        steps: [
            {
                id: 1,
                title: "Personal Information",
                icon_class: "fa fa-user-circle-o"
            },
            {
                id: 2,
                title: "Educational Background",
                icon_class: "fa fa-graduation-cap"
            },
            {
                id: 3,
                title: "Profesionnal Background",
                icon_class: "fa fa-briefcase"
            }
        ]
    },

    methods: {
        stepChanged(step) {
            this.currentstep = step;
        }
    }
});