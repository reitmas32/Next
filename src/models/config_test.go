package models

import (
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLoadFromFile(t *testing.T) {
	// Crear un archivo de prueba temporal con datos YAML
	yamlData := `
		name: Mi Aplicación
		version:
		version: 0.1.0
		description: Una descripción
		`
	filename := "test_config.yaml"
	err := os.WriteFile(filename, []byte(yamlData), 0644)
	if err != nil {
		t.Fatalf("Error creando el archivo de prueba: %v", err)
	}
	defer os.Remove(filename)

	// Crear una instancia de Config y cargar desde el archivo
	config := &Config{}
	err = config.LoadFromFile(filename)

	// Verificar que no haya errores y que los campos se carguen correctamente
	assert.NoError(t, err)
	assert.Equal(t, "Mi Aplicación", config.Name)
	assert.Equal(t, "0.1.0", config.Version)
	assert.Equal(t, "Una descripción", config.Description)
}

func TestLoadFromString(t *testing.T) {
	// Cadena YAML de prueba
	yamlString := `
		name: Otra Aplicación
		version:
		version: 2.0.0
		description: Otra descripción
		`

	// Crear una instancia de Config y cargar desde la cadena
	config := &Config{}
	err := config.LoadFromString(yamlString)

	// Verificar que no haya errores y que los campos se carguen correctamente
	assert.NoError(t, err)
	assert.Equal(t, "Otra Aplicación", config.Name)
	assert.Equal(t, "2.0.0", config.Version)
	assert.Equal(t, "Otra descripción", config.Description)
}

func TestLoadFromFile_InvalidFile(t *testing.T) {
	// Intentar cargar desde un archivo inexistente
	config := &Config{}
	err := config.LoadFromFile("archivo_inexistente.yaml")

	// Verificar que se produzca un error
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "no such file or directory")
}

func TestLoadFromString_InvalidYAML(t *testing.T) {
	// Cadena YAML inválida
	invalidYAML := `
		name: Mi Aplicación
		version: 0.1.0
		description: Una descripción
		`

	// Crear una instancia de Config y cargar desde la cadena inválida
	config := &Config{}
	err := config.LoadFromString(invalidYAML)

	// Verificar que se produzca un error debido al formato YAML incorrecto
	assert.Error(t, err)
	assert.Contains(t, err.Error(), "yaml: unmarshal errors")
}
