package views

import (
	"github.com/reitmas32/Next/src/commands"
	"github.com/spf13/cobra"
)

var CreateCommand = &cobra.Command{
	Use:     "create",
	Aliases: []string{"c"},
	Short:   "Create Current Proyect",
	Run:     commands.Create,
}
