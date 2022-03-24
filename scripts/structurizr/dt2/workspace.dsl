
workspace "SystemLandscape" ""{
    model {
        user = person "Internal User" "End User" "Customer"
        frontEnd = softwareSystem "Front End React" "Base web app" "Front End"
        backEnd = softwareSystem "Node Backend" "Simple backend" "Back End"
        datasource = softwareSystem "Simulation Engine Output" "Excel Data" "Database"
        simulationEngine = softwareSystem "Simulation Engine" "DS backend" "Back End"

        user -> frontEnd "visits"
        frontEnd -> backEnd "gets processed data"
        backEnd -> datasource "collects from"
        simulationEngine -> datasource "generates"

    }

    views {
        systemlandscape "SystemLandscape" {
            include *
            autoLayout lr
        }


        styles {
            element "Customer"{
                shape Person
            }
            element "Front End" {
                shape WebBrowser
            }
            element "Database" {
                shape Component
            }
    	    element "Software System" {

                background #4b5320
                color #ffffff
            }
        }
    }
}


