package views

import (
	"github.com/reitmas32/Next/src/commands"
	"github.com/spf13/cobra"
)

var VersionCommand = &cobra.Command{
	Use:     "version",
	Aliases: []string{"v"},
	Short:   "Print the version of Next",
	Run:     commands.Version,
}
