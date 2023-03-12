workspace "SystemLandscape" ""{
    model {
        softwareSystemFE = softwareSystem "Shopping Cart FE" {
        }
        softwareSystemApiGateway = softwareSystem "API Gateway" {
        }
        softwareSystemPayment = softwareSystem "Payment Integration" {
        }
        softwareSystemUserAuth = softwareSystem "User Authentication" {
        }
        softwareSystemDelivery = softwareSystem "Delivery System" {
        }
        softwareSystemStockManagement = softwareSystem "Stock Management" {
        }
      
        softwareSystemFE -> softwareSystemApiGateway
        softwareSystemApiGateway -> softwareSystemPayment
        softwareSystemApiGateway -> softwareSystemUserAuth
        softwareSystemApiGateway -> softwareSystemDelivery
        softwareSystemApiGateway -> softwareSystemStockManagement
    }

    views {
       systemContext softwareSystemApiGateway {
           include *
           autolayout tb 300 300
        }


        styles {
            element "Customer"{
                shape Person
            }
            element "Front End" {
                shape WebBrowser
            }
            element "Database" {
                shape Cylinder
            }
            element "Software System" {
                color "#ffffff"
            }
            element "India" {
                background "#fff3bf"
                color "#000000"
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



