CREATE_TABLE "Role"(
    "id" TEXT PRIMARY KEY,
    "name" TEXT UNIQUE,
    "permissions" TEXT,
    "createAt" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME
);

CREATE_TABLE "Vacc"(
    "id" TEXT PRIMARY KEY,
    "name" TEXT UNIQUE,
    "website" TEXT,
    "contactEmail" TEXT,
    "createAt" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "updateAt" DATETIME
);

CREATE TABLE "User" (
    "id" TEXT PRIMARY KEY,
    "name" TEXT,
    "ratingId" INTEGER,
    "ratingShort" TEXT,
    "ratingLong" TEXT,
    "region" TEXT,
    "division" TEXT,
    "roleIds" TEXT,
    "vaccId" TEXT,
    "createdAt" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME,
    FOREIGN KEY ("vaccId") REFERENCES "Vacc"("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "AuditLogEntry"(
    "id" TEXT PRIMARY KEY,
    "timestamp" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "actor" TEXT,
    "item" TEXT,
    "before" TEXT,
    "after" TEXT,
    "message" TEXT
);

CREATE TABLE "TrainingQueue"(
    "id" TEXT PRIMARY KEY,
    "vaccId" TEXT,
    "name" TEXT,
    "name" TEXT,
    "description" TEXT,
    "joinableByDefault" BOOLEAN,
    "createdAt" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME,
    FOREIGN KEY ("vaccId") REFERENCES "Vacc"("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "TrainingQueueMembership"(
    "userId" TEXT,
    "queueId" TEXT,
    "joinedAt" DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ("userId", "queueId"),
    FOREIGN KEY ("userId") REFERENCES "User" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY ("queueId") REFERENCES "TrainingQueue" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "Certificate" (
    "holderId" TEXT,
    "instructorId" TEXT,
    "position" TEXT,
    "expires" DATETIME,
    "instructorComments" TEXT,
    "createdAt" DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ("holderId", "instructorId", "position"),
    FOREIGN KEY ("holderId") REFERENCES "User" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY ("instructorId") REFERENCES "User" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "Resource"(
    "id" TEXT PRIMARY KEY,
    "vaccId" TEXT,
    "isStaffOnly" BOOLEAN,
    "name" TEXT,
    "descriptino" TEXT,
    "link" TEXT,
    FOREIGN KEY ("vaccId") REFERENCES "Vacc" ("id") ON DELETE SET NULL ON UPDATE CASCADE,
);

CREATE TABLE "Session"(
    "id" TEXT PRIMARY KEY,
    "studentId" TEXT,
    "instructorId" TEXT,
    "sessionType" TEXT,
    "date" DATETIME,
    "studentComments" TEXT,
    "instructorComments" TEXT,
    "createdAt" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME,
    FOREIGN KEY ("studentId") REFERENCES "User" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY ("instructorId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE "Connection"(
    "id" TEXT PRIMARY KEY,
    "userId" TEXT,
    "callSign" TEXT,
    "isAuthorized" BOOLEAN,
    "startTime" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "endTime" DATETIME,
    FOREIGN KEY ("userId") REFERENCES "User" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
)