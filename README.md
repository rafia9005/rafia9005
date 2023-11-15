```golang
package main

import (
	"github.com/gofiber/fiber/v2"
	"net/http"
)

type FullStackDeveloper struct {
	Nama       string `json:"nama"`
	Posisi     string `json:"posisi"`
	Pendidikan string `json:"pendidikan"`
	Site       string `json:"site"`
}

func main() {
	app := fiber.New()

	app.Get("/profil", func(c *fiber.Ctx) error {
		fullStackDeveloper := FullStackDeveloper{
			Nama:       "Ahmad Rafi",
			Posisi:     "Full Stack Developer",
			Pendidikan: "Sistem Informasi Jaringan & Aplikasi",
			Site:       "www.rafii.site",
		}

		return c.JSON(fullStackDeveloper)
	})

	app.Listen(":8080")
}
