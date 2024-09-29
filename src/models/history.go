package models

type History struct {
	BaseModel
	Id            int    `gorm:"primary_key;autoIncrement" json:"id"`
	MediaId       string `gorm:"type:varchar(255)" json:"mediaId"`
	Name          string `gorm:"type:varchar(255)" json:"name"`
	Type          string `gorm:"type:varchar(255)" json:"type"`
	SeasonNumber  int    `gorm:"type:int" json:"seasonNumber"`
	EpisodeNumber int    `gorm:"type:int" json:"episodeNumber"`
	ProfileId     int    `gorm:"type:int" json:"profileId"`
	PrevCodec     string `gorm:"type:varchar(255)" json:"prevCodec"`
	NewCodec      string `gorm:"type:varchar(255)" json:"newCodec"`
	PrevSize      int    `gorm:"type:int" json:"prevSize"`
	NewSize       int    `gorm:"type:int" json:"newSize"`
	Date          string `gorm:"type:varchar(255)" json:"date"`
}
