
workspace "SystemLandscape" ""{
    model {
        Input = person "Manual Input" "Input" "Customer"
        Output = person "Me" "Output" "Customer"

        Readwise = softwareSystem "Readwise" "Aggregator" "Pipe"
        Goodreads = softwareSystem "Goodreads" "Website" "Software System"
        KindleScribe = softwareSystem "Kindle Scribe" "Books" "Software System"
        PhysicalBooks = element "Physical Books" "ASDSAD" "Front End"


        RSSFeed = softwareSystem "Inoreader RSS Reader" "RSS Reader" "Pipe"
        CodingHorror = softwareSystem "Coding Horror Blog" "Blog site" "Front End"
        StackOverflowBlog = softwareSystem "StackOverflow Blog" "Blog site" "Front End"
        ThoughWorksRadar = softwareSystem "ThoughtWorks Radar Blog" "Blog site" "Front End"

        Obsidian = softwareSystem "Obsidian" "Note Taking Tool" "Component"
        Git  = softwareSystem "Git" "Sync" "Cylinder"

        OpenAI  = softwareSystem "Open AI" "GPT-3" "Robot"

        Input -> Obsidian "manual input of other notes"
        Input -> PhysicalBooks "manual processing"


        CodingHorror -> RSSFeed "pulls new articles"
        StackOverflowBlog -> RSSFeed "pulls new articles"
        ThoughWorksRadar -> RSSFeed "pulls new articles"
        RSSFeed -> Readwise "pulls all information"

        Goodreads -> Readwise "pulls all information"
        KindleScribe -> Readwise "pulls all information"
        PhysicalBooks -> Readwise "manual input"

        Readwise -> Obsidian "pulls"
        Obsidian -> Git "Syncs all my notes"
        Obsidian -> OpenAI "Synthesize & Help Generate Ideas"
        OpenAI -> Output "Consume"

    }


    views {
        systemlandscape "SystemLandscape" {
            include *
            autoLayout
        }


        styles {
            element "Customer"{
                shape Person
            }
            element "Pipe"{
                background #8F7D7D
                shape Pipe
            }
            element "Robot"{
                background #B19E9E
                shape Robot
            }
            element "Component"{
                background #8F7D7D
                shape Component
            }
             element "Cylinder"{
                background #8F7D7D
                shape Cylinder
            }
            element "Front End" {
                background #6D5C5C
                shape WebBrowser
            }
            element "Folder" {
                shape Folder
            }
	        element "Software System" {
                background #4A3A3A
                color #ffffff
            }
        }
    }
}


