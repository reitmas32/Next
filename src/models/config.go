package models

import (
	"errors"
	"fmt"
	"os"

	"github.com/reitmas32/Next/src/validators"
	"gopkg.in/yaml.v2"
)

type Config struct {
	Name         string                 `yaml:"name"`
	Version      string                 `yaml:"version"`
	Description  string                 `yaml:"description"`
	TypeProject  string                 `yaml:"type_project"`
	BuildDir     string                 `yaml:"build_dir"`
	Dependencies map[string]Dependencie `yaml:"dependencies"`
}

func (c *Config) LoadFromFile(filename string) error {
	yamlFile, err := os.ReadFile(filename)
	if err != nil {
		return err
	}

	err = yaml.Unmarshal(yamlFile, c)
	if err != nil {
		return errors.New(fmt.Sprintf("err.Error(): %v in %s\n", err.Error(), filename))
	}

	result := validators.ValidateVersion(c.Version)
	if !result {
		return errors.New(fmt.Sprintf("err.Error(): Invalid Format Version in %s\n", filename))

	}

	err = validators.ValidateTypeProject(c.TypeProject)
	if err != nil {
		return errors.New(fmt.Sprintf("err.Error(): %v in %s\n", err.Error(), filename))
	}

	for name := range c.Dependencies {
		// Verificar si la dependencia existe
		if dependencie, ok := c.Dependencies[name]; ok {
			// Eliminar la entrada antigua del mapa
			delete(c.Dependencies, name)

			// Cambiar el nombre de la dependencia
			dependencie.Name = name

			// Agregar la entrada actualizada al mapa
			c.Dependencies[name] = dependencie

		}
	}

	return nil
}

func (c *Config) LoadFromString(yamlString string) error {
	err := yaml.Unmarshal([]byte(yamlString), c)
	if err != nil {
		return err
	}
	return nil
}

func (c *Config) SaveToFile(filename string) error {
	// Convierte el objeto Config a YAML
	yamlData, err := yaml.Marshal(c)
	if err != nil {
		return err
	}

	// Escribe el YAML en el archivo
	err = os.WriteFile(filename, yamlData, 0644)
	if err != nil {
		return err
	}

	return nil
}

func (c *Config) ToString() (string, error) {
	yamlBytes, err := yaml.Marshal(c)
	if err != nil {
		return "", err
	}
	return string(yamlBytes), nil
}
