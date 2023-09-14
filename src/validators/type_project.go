package validators

import (
	"errors"
	"regexp"
)

func ValidateTypeProject(version string) error {
	// Define una expresión regular para verificar el formato.
	validFormat := regexp.MustCompile(`^(executable|static_library|dynamic_library)$`)

	// Convierte el texto en una cadena.
	versionStr := string(version)

	// Verifica si el formato es válido.
	if !validFormat.MatchString(versionStr) {
		return errors.New("The typeProject format is not valid use (executable | static_library | dynamic_library) in the")
	}

	return nil
}
