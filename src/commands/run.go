package commands

import (
	"fmt"

	"github.com/spf13/cobra"
)

func Run(cmd *cobra.Command, args []string) {
	fmt.Println("Run Command")
}