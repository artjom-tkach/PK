CREATE TABLE "Users" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL UNIQUE,
	"role_id"	INTEGER,
	"first_name"	VARCHAR(255) NOT NULL,
	"last_name"	VARCHAR(255),
	"username"	VARCHAR(255) UNIQUE,
	"language_code"	VARCHAR(255) DEFAULT 'en',
	"is_blocked"	INTEGER DEFAULT 0 CHECK("is_blocked" IN (0, 1)),
	"acted_at"	VARCHAR(255),
	"created_at"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("role_id") REFERENCES "RoleUsers"("id")
)