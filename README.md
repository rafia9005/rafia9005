```golang
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	r.GET("/profil", func(c *gin.Context) {
		fullStackDeveloper := FullStackDeveloper{
			Nama:       "Ahmad Rafi",
			Posisi:     "Full Stack Developer",
			Pendidikan: "Sistem Informasi Jaringan & Aplikasi",
			Site:       "www.rafii.site",
		}

		c.JSON(http.StatusOK, gin.H{
			"profil": fullStackDeveloper,
		})
	})

	r.Run(":8080")
}

