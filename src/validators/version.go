package validators

import (
	"regexp"
)

func ValidateVersion(version string) bool {
	// Define una expresión regular para verificar el formato.
	validFormat := regexp.MustCompile(`^[0-9]+(\.[0-9]+)*$|latest`)

	// Convierte el texto en una cadena.
	versionStr := string(version)

	// Verifica si el formato es válido.
	if !validFormat.MatchString(versionStr) {
		return false
	}

	return true
}
