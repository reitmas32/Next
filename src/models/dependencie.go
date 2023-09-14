package models

import (
	"strings"

	"github.com/reitmas32/Next/src/validators"
)

type Dependencie struct {
	Name    string `yaml:"name"`
	Version string `yaml:"version"`
	Dir     string `yaml:"dir"`
	Build   string `yaml:"build"`
}

func (d *Dependencie) UnmarshalText(text []byte) error {

	// Divide el string en palabras utilizando ":" como separador
	palabras := strings.Split(string(text), ":")

	//Solo tiene version o repo
	if len(palabras) == 1 {

		palabra := palabras[0]
		// Solo tiene version
		if validators.ValidateVersion(palabra) {
			d.Version = palabra
			return nil
		}
		//Solo tiene direccion de github
		d.Dir = palabra
		d.Version = "latest"
	}
	if len(palabras) == 2 {

		palabra := palabras[0]
		// Solo tiene version
		if validators.ValidateVersion(palabra) {
			d.Version = palabra
			return nil
		}
		//Solo tiene direccion de github
		d.Dir = palabra
		d.Version = "latest"
		d.Build = palabras[1]
		return nil
	}
	if len(palabras) == 3 {

		d.Dir = palabras[0]
		d.Version = palabras[1]
		d.Build = palabras[2]
		return nil
	}

	return nil
}
