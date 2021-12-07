workspace "SystemLandscape" ""{
    model {
        user = person "Client" "Bank Client" "Customer"
        frontEnd = softwareSystem "User Interface" "Web App or Mobile App" "Front End"
        graphQL = softwareSystem "GraphQL Gateway" "GraphQL Gateway" "GraphQL"
        authService = softwareSystem "Auth Service" "Authenticates Request" "Back End"
        
        fileManagement = softwareSystem "File Management System" "File Management System" "Back End"{
            uploadService = container "Upload Service Controller" "Handles all upload mechanism and metadata generation" "NestJS" "Back End"
            lifeCycleManagement = container "Life Cycle Controller" "Handles expiry and cleanup mechanisms versus offloading to cloud provider" "Worker" "Event Driven"
            fileManagementDatabase = container "Upload DB" "Contains all metadata of all files managed" "Postgres" "Database"
            encryptionAgent = container "Encryption Controller" "Allows user to encrypt custom way" "Nest JS/GPG/SSH" "Back End"
        }
        ocrService = softwareSystem "OCR Service" "OCR Service" "Back End"{
            # ocrServiceContainer = container "OCR Service" "Handles OCR request" "NestJS" "Back End"
        }
        # ocrProvider = softwareSystem "3rd Party OCR Provider" "Google lens" "External"
        
    
        cloudProvider = softwareSystem "3rd Party File Storage Cloud Provider" "AWS/Azure/Adobe File Manager" "External"
        
        # Top Level Relationships
        user -> frontEnd "access"
        frontEnd -> graphQL "mutation: uploadFile"
        graphQL -> authService "validate user request" "HTTP POST"
        graphQL -> fileManagement "uploads files"
        fileManagement -> graphQL "gets file metadata" "HTTP GET"
        fileManagement -> cloudProvider "stores files in" "multipart upload"
        ocrService -> cloudProvider "validates files"
        graphQL -> ocrService "get OCR Request" "Event Driven"
        ocrService -> graphQL "OCR Details"
        
        
        # Container Relationships
        uploadService -> cloudProvider "stores files in" "multipart upload"
        graphQL -> uploadService "uploads files" "multipart upload"
        graphQL -> encryptionAgent "upload keys" "SSH/GPG"
        lifeCycleManagement -> cloudProvider "performs cleanup" "batch processing"
        uploadService -> fileManagementDatabase "saves file metadata" "ORM"
        fileManagementDatabase -> lifeCycleManagement "Gets file metadata"
        uploadService -> encryptionAgent "Encrypts file"
        
        # ocrServiceContainer -> ocrProvider "send requests"
    }

    views {
        systemlandscape "SystemLandscape" {
            include *
            autolayout
        }
              
        container fileManagement "File_Management_Containers" {
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


