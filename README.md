[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/p9VNMUI0)
# Trabajo integrador de segundo semestre
El objetivo de este trabajo integrador es proporcionar a los estudiantes de segundo nivel de desarrollo de software una experiencia práctica que combine los conocimientos adquiridos en los cursos de Programación II y Bases de Datos I. A través de este proyecto, los estudiantes desarrollarán una aplicación web utilizando Django, HTML, CSS y JavaScript, aplicando principios de la programación orientada a objetos y el modelo vista-controlador. Además, implementarán una base de datos relacional en PostgreSQL, diseñando el diagrama lógico, creando las tablas con sus respectivas relaciones y validando la integridad de los datos mediante restricciones y llaves.

Este trabajo integral permite a los estudiantes aplicar y consolidar sus conocimientos en dos áreas fundamentales del desarrollo de software: la programación y la gestión de bases de datos. Los estudiantes deberán desarrollar un catálogo temático que integre los conocimientos de ambas asignaturas, mediante el análisis y desarrollo de la gestión de productos y compras, y generación de reportes.

La implementación completa de este proyecto demostrará la capacidad de los estudiantes para desarrollar aplicaciones robustas y eficientes, conectadas a una base de datos relacional, fortaleciendo así su preparación para desafíos profesionales futuros.

## Nombres de los estudiantes

Jeremy Marin
Jhosue Lopez

## Tener en cuenta

Este programa usa funciones en la base de datos que deben ser creadas manualmente, no olvidar de cambiar las opciones de la base de datos en el setting.

CREATE OR REPLACE FUNCTION validate_dni(cedula VARCHAR) RETURNS BOOLEAN AS $$
DECLARE
    total INTEGER;
    digito_verificador INTEGER;
    i INTEGER;
    suma INTEGER;
BEGIN
    -- Validar longitud
    IF LENGTH(cedula) != 10 THEN
        RETURN FALSE;  -- La cédula debe tener exactamente 10 dígitos
    END IF;
    
    -- Validar que todos los caracteres sean dígitos
    IF NOT cedula ~ '^\d{10}$' THEN
        RETURN FALSE;  -- La cédula debe contener solo dígitos
    END IF;

    -- Extraer el dígito verificador
    digito_verificador := CAST(SUBSTRING(cedula FROM 10 FOR 1) AS INTEGER);

    -- Calcular la suma para verificar la cédula
    suma := 0;
    FOR i IN 1..9 LOOP
        IF i % 2 = 1 THEN
            total := CAST(SUBSTRING(cedula FROM i FOR 1) AS INTEGER) * 2;
            IF total > 9 THEN
                total := total - 9;
            END IF;
        ELSE
            total := CAST(SUBSTRING(cedula FROM i FOR 1) AS INTEGER);
        END IF;
        suma := suma + total;
    END LOOP;

    -- Calcular el dígito verificador esperado
    total := (10 - (suma % 10)) % 10;

    -- Comparar el dígito verificador calculado con el proporcionado
    RETURN digito_verificador = total;  -- Devuelve TRUE si la cédula es válida, FALSE si no lo es
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION validate_phone_number(telefono TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    -- Verifica que el número de teléfono comience con '09' y tenga exactamente 10 dígitos
    IF telefono ~ '^09\d{8}$' THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$$ LANGUAGE plpgsql;


