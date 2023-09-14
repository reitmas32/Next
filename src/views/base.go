package views

import (
	"github.com/reitmas32/Next/src/config"
	"github.com/spf13/cobra"
)

func LoadViews() {
	//Hiden Completion Command
	completion := &cobra.Command{
		Use:   "completion",
		Short: "Generate the autocompletion script for the specified shell",
	}

	// mark completion hidden
	completion.Hidden = true
	config.RootCommand.AddCommand(completion)

	//Version
	config.RootCommand.AddCommand(VersionCommand)
}
