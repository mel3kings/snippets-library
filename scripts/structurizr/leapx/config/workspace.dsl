
workspace "SystemLandscape" "Microservice Restart"{
    model {
       ms1 = softwareSystem "Microservice1" "Microservice v1.0" "India"
       ms3 = softwareSystem "Microservice3" "Microservice v3.0" "India"

       ms7 = softwareSystem "Microservice7" "Microservice v1.0.0" "EU"
       ms8 = softwareSystem "Microservice8" "Microservice v1.0.1" "EU" 
       configServer = softwareSystem "Config Server" "Config Server" "Backend"
       
      
        
        ms1 -> configServer "Get initial config" "HTTP GET"
        ms3 -> configServer "Get initial config" "HTTP GET"
        ms7 -> configServer "Get initial config" "HTTP GET"
        ms8 -> configServer "Get initial config" "HTTP GET"
     
     
    }

    views {
        systemlandscape "SystemLandscape" "Microservice Restart" {
            include *
            autoLayout lr
        }


        styles {
            element "Customer"{
                shape Person
            }
            element "Kafka"{
                shape Pipe
            }
            element "Front End" {
                shape WebBrowser
            }
            element "Database" {
                shape Cylinder
            }
            element "Software System" {
                color #ffffff
            }
            element "India" {
                background "#fff3bf"
                color "#000000"
            }
             element "Anti" {
                color "#000000"
                background "#ff6b6b"
            }
            element "Sydney"{
                background "#ccedff"
                color "#000000"
            }
            element "EU" {
                background "#e6fcf5"
                color "#000000"
            }

        }

         theme default

    }
}





