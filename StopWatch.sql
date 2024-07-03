-- Crear base de datos y usarla
CREATE DATABASE StopWatch;
GO
USE StopWatch;
GO

-- Crear tabla Category

CREATE TABLE Category (
    id INT IDENTITY(1,1),
    categoryName VARCHAR(20),
    number INT,
    PRIMARY KEY(id)
);

-- Crear tabla Driver

CREATE TABLE Driver (
    id INT IDENTITY(1,1),
    driverName VARCHAR(255),
    email VARCHAR(255),
    age INT,
    PRIMARY KEY(id)
);

-- Crear tabla Kart

CREATE TABLE Kart (
    id INT IDENTITY(1,1),
    numero INT,
    color VARCHAR(255),
    frontLeftPressure FLOAT(2),
    frontRightPressure FLOAT(2),
    rearLeftPressure FLOAT(2),
    rearRightPressure FLOAT(2),
    PRIMARY KEY(id)
);

-- Crear tabla Lap

CREATE TABLE Lap (
    id INT IDENTITY(1,1),
    lapStart BIGINT,
    lapEnd BIGINT,
    PRIMARY KEY(id)
);

-- Crear tabla Split

CREATE TABLE Split (
    id INT IDENTITY(1,1),
    splitStart BIGINT,
    splitEnd BIGINT,
    lapId INT,
    PRIMARY KEY(id),
    CONSTRAINT FK_SplitLap 
		FOREIGN KEY (lapId) REFERENCES Lap(id)
);

-- Crear tabla Race

CREATE TABLE Race (
    id INT IDENTITY(1,1),
    raceName VARCHAR(20),
    lapId INT,
    PRIMARY KEY(id),
    CONSTRAINT FK_RaceLap 
		FOREIGN KEY (lapId) REFERENCES Lap(id)
);

-- Crear tabla Stopwatch

CREATE TABLE Stopwatch (
    id INT IDENTITY(1,1),
    stopwatchName VARCHAR(20),
    driverId INT,
    kartId INT,
    categoryId INT,
    raceId INT,
    PRIMARY KEY(id),
    CONSTRAINT FK_StopwatchDriver 
		FOREIGN KEY (driverId) REFERENCES Driver(id),
    CONSTRAINT FK_StopwatchKart 
		FOREIGN KEY (kartId) REFERENCES Kart(id),
    CONSTRAINT FK_StopwatchCategory 
		FOREIGN KEY (categoryId) REFERENCES Category(id),
    CONSTRAINT FK_StopwatchRace 
		FOREIGN KEY (raceId) REFERENCES Race(id)
);

-- Insertar datos en la tabla Category

INSERT INTO Category (categoryName, number)
VALUES ('DD2', 1),
       ('DD2 Master', 2),
       ('Junior', 3);

-- Insertar datos en la tabla Driver

INSERT INTO Driver (driverName, email, age)
VALUES ('Juan Perez', 'juan.perez@example.com', 30),
       ('Maria Gomez', 'maria.gomez@example.com', 22),
       ('Carlos Ruiz', 'carlos.ruiz@example.com', 28);

-- Insertar datos en la tabla Kart

INSERT INTO Kart (numero, color, frontLeftPressure, frontRightPressure, rearLeftPressure, rearRightPressure)
VALUES (1, 'Rojo', 32.5, 32.6, 32.7, 32.8),
       (2, 'Azul', 32.4, 32.3, 32.6, 32.7),
       (3, 'Verde', 32.6, 32.5, 32.8, 32.9);

-- Insertar datos en la tabla Lap
INSERT INTO Lap (lapStart, lapEnd)
VALUES (0, 1200),
       (0, 1100),
       (0, 2000);

-- Insertar datos en la tabla Race (correctas referencias a Lap)

INSERT INTO Race (raceName, lapId)
VALUES ('Race1', 3),
       ('Race2', 4),
       ('Race3', 5);

-- Insertar datos en la tabla Split (correctas referencias a Lap)

INSERT INTO Split (splitStart, splitEnd, lapId)
VALUES (101, 1000, 4),
       (70, 1200, 5),
       (60, 1500, 6);


-- Insertar datos en la tabla Stopwatch (correctas referencias a Race)

INSERT INTO Stopwatch (stopwatchName, driverId, kartId, categoryId, raceId)
VALUES ('Stopwatch4', 1, 1, 1, 4),
       ('Stopwatch5', 2, 2, 3, 5),
       ('Stopwatch6', 3, 3, 1, 6);

-- a) Consulta de conductores mayores de 25 años

SELECT *
FROM Driver
WHERE age > 25;

-- b) Mejor y peor tiempo por categoría y conductor

SELECT 
    c.categoryName,
    d.driverName,
    MIN(l.lapEnd - l.lapStart) AS bestTime,
    MAX(l.lapEnd - l.lapStart) AS worstTime
FROM 
    Stopwatch s
    JOIN Driver d ON s.driverId = d.id
    JOIN Category c ON s.categoryId = c.id
    JOIN Race r ON s.raceId = r.id
    JOIN Lap l ON r.lapId = l.id
GROUP BY 
    c.categoryName,
    d.driverName;

-- c) Mínimo tiempo de segmento por conductor

SELECT 
    d.driverName,
    MIN(sp.splitEnd - sp.splitStart) AS minSplitTime
FROM 
    Stopwatch s
    JOIN Driver d ON s.driverId = d.id
    JOIN Race r ON s.raceId = r.id
    JOIN Lap l ON r.lapId = l.id
    JOIN Split sp ON l.id = sp.lapId
GROUP BY 
    d.driverName
ORDER BY 
    minSplitTime;

-- d) Mejor tiempo de vuelta en general

SELECT TOP 1
    d.driverName,
    l.lapEnd - l.lapStart AS lapTime
FROM 
    Stopwatch s
    JOIN Driver d ON s.driverId = d.id
    JOIN Race r ON s.raceId = r.id
    JOIN Lap l ON r.lapId = l.id
ORDER BY 
    lapTime;

-- e) Selección de todos los datos de la tabla Stopwatch

SELECT *
FROM Stopwatch;
