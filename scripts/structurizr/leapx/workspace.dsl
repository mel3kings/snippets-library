workspace "SystemLandscape" ""{
    model {
        user = person "Client" "Bank Client" "Customer"
        frontEnd = softwareSystem "User Interface" "Web App or Mobile App" "Front End"
        graphQL = softwareSystem "GraphQL Gateway" "GraphQL Gateway" "GraphQL"
        authService = softwareSystem "Auth Service" "Authenticates Request" "Back End"
        
        fileManagement = softwareSystem "File Management System" "File Management System" "Back End"{
            uploadService = container "Upload Service Container" "Handles all upload mechanism and metadata generation" "NestJS" "Back End"{
                uploadServiceController = component "Upload Service Controller" "Upload Controller" "NestJS" "Back End"
                encryptionAgent = component "Encryption Controller" "Allows user to encrypt custom way" "Nest JS/GPG/SSH" "Back End"
                lifeCycleManagement = component "Life Cycle Controller" "Handles expiry and cleanup mechanisms versus offloading to cloud provider" "Worker" "Event Driven"
            }
            fileManagementDatabase = container "Upload DB" "Contains all metadata of all files managed" "Postgres" "Database"
            
            
        }
        ocrService = softwareSystem "OCR Service" "OCR Service" "Back End"{
            # ocrServiceContainer = container "OCR Service" "Handles OCR request" "NestJS" "Back End"
        }
        # ocrProvider = softwareSystem "3rd Party OCR Provider" "Google lens" "External"
        
    
        cloudProvider = softwareSystem "3rd Party File Storage Cloud Provider" "AWS/Azure/Adobe File Manager" "External"
        
        # Top Level Relationships
        user -> frontEnd "1. access"
        frontEnd -> graphQL "2. mutation: uploadFile"
        graphQL -> authService "3. validate user request" "HTTP POST"
        graphQL -> fileManagement "4. uploads files"
        fileManagement -> cloudProvider "5. stores files in" "multipart upload"     
        fileManagement -> graphQL "6. gets file metadata" "HTTP GET"
        graphQL -> ocrService "7. get OCR Request" "Event Driven"
        ocrService -> cloudProvider "8. validates files"
        ocrService -> graphQL "9. OCR Details"
        graphQL -> frontEnd "10. Return file and OCR details"
        
        
        # Container Relationships
        uploadService -> cloudProvider "stores files in" "multipart upload"
        graphQL -> uploadService "uploads files" "multipart upload"
        graphQL -> encryptionAgent "upload keys" "SSH/GPG"
        lifeCycleManagement -> cloudProvider "performs cleanup" "batch processing"
        uploadServiceController -> fileManagementDatabase "saves file metadata" "ORM"
        fileManagementDatabase -> lifeCycleManagement "Gets file metadata"
        uploadServiceController -> encryptionAgent "Encrypts file"
        
        # ocrServiceContainer -> ocrProvider "send requests"
    }

    views {
        systemlandscape "SystemLandscape" {
            include *
            autolayout tb
        }
              
         component uploadService "File_Management_Controllers" {
                    include *
                    autoLayout lr
         }
        
        
        styles {
            element "Customer"{
                shape Person
            }
            element "GraphQL"{
                shape Hexagon
            }
            element "Front End" {
                shape WebBrowser
            }
            element "Event Driven" {
                shape RoundedBox
            }
            element "External"{
                shape Component
                background #868e96
            }
            element "Database" {
                shape Cylinder
            }
	        element "Software System" {
                background #1168bd
                color #ffffff
            }
        }
    }
}


