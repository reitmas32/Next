package commands

import (
	"fmt"

	"github.com/spf13/cobra"
)

const version = "0.0.1"
const date = "13-09-2023"
const opyright = "Copyright (C) 2023 Next"

func Version(cmd *cobra.Command, args []string) {
	if len(args) != 1 {
		fmt.Printf("%s\n", version)

	} else if args[0] == "v" || args[0] == "V" {
		//Verbose output
		fmt.Printf("nx %s release %s\n", version, date)
		fmt.Println("Copyright (C) 2023 Next")
	}
}
