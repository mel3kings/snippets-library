
workspace "SystemLandscape" ""{
    model {
        mckinsey = person "McKinsey" "Consultant" "Customer"
        defenceUser = softwareSystem "Client Approved Authentication" "SSH or Service Account (TBC)" "Component"
        mckinseyRepository = softwareSystem "Internal Private McKinsey Repository" "GitHub" "Software System"
        defenceArtifactory = softwareSystem "Client Internal Artifactory" "JFrog" "Software System"
        PRN = softwareSystem "Private Client Internal Network" "PRN" "VM"

        mckinsey -> mckinseyRepository "1. pushes code to"
        mckinseyRepository -> mckinseyRepository "2. Scans code and commits logs"
        defenceUser -> defenceArtifactory ""
       
        mckinseyRepository -> defenceUser "3. Automated code pulls"
        
        defenceArtifactory -> defenceArtifactory "4. Scans code"
        defenceArtifactory -> PRN "5. pull artefacts from"


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
             element "VM" {
                shape RoundedBox
             }
             element "Component" {
                color #000000
                background #dee2e6
                shape Component
             }
            element "Database" {
                shape Cylinder
            }
	    element "Software System" {
                background #1168bd
                color #ffffff
                shape Cylinder
            }
        }
    }
}
