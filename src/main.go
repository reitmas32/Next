package main

import (
	"fmt"
	"os"

	"github.com/reitmas32/Next/src/config"
	"github.com/reitmas32/Next/src/views"
)

func main() {
	views.LoadViews()

	if err := config.RootCommand.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

}
