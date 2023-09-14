package config

import "github.com/spf13/cobra"

var RootCommand = &cobra.Command{
	Use:   "nx",
	Short: "Manage your Next app development.",
}
