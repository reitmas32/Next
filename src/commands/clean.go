package commands

import (
	"fmt"

	"github.com/spf13/cobra"
)

func Clean(cmd *cobra.Command, args []string) {
	fmt.Println("Clean Command")
}
