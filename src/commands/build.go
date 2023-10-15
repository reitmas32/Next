package commands

import (
	"fmt"

	"github.com/spf13/cobra"
)

func Build(cmd *cobra.Command, args []string) {
	fmt.Println("Build Command")
}
