package main

import (
	"transfigurr/startup"
)

func main() {

	db, scanService, encodeService, metadataService, seriesRepo, seasonRepo, episodeRepo, movieRepo, settingRepo, systemRepo, profileRepo, authRepo, userRepo, historyRepo, eventRepo, codecRepo := startup.Startup()
	router := SetupRouter(scanService, encodeService, metadataService, seriesRepo, seasonRepo, episodeRepo, movieRepo, settingRepo, systemRepo, profileRepo, authRepo, userRepo, historyRepo, eventRepo, codecRepo)
	// Get the underlying sql.DB and defer its close
	sqlDB, err := db.DB()
	if err != nil {
		return
	}
	defer sqlDB.Close()

	router.Run("0.0.0.0:7889")

}
