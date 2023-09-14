package models

import (
	"errors"
	"fmt"
	"os"
	"regexp"

	"gopkg.in/yaml.v2"
)

type Config struct {
	Name        string `yaml:"name"`
	Version     string `yaml:"version"`
	Description string `yaml:"description"`
}

func (c *Config) LoadFromFile(filename string) error {
	yamlFile, err := os.ReadFile(filename)
	if err != nil {
		return err
	}

	err = yaml.Unmarshal(yamlFile, c)
	if err != nil {
		return err
	}

	// Define una expresión regular para verificar el formato.
	validFormat := regexp.MustCompile(`^[0-9]+(\.[0-9]+)*$`)

	// Convierte el texto en una cadena.
	versionStr := string(c.Version)

	// Verifica si el formato es válido.
	if !validFormat.MatchString(versionStr) {
		return errors.New(fmt.Sprintf("The version format is not valid in the %s", filename))
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
