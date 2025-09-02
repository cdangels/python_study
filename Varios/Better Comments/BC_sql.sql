/* ===== SQL ===== */
-- ! Consulta crítica para producción
-- ? ¿Debería usar INNER o LEFT JOIN?
-- TODO: Agregar índice en esta columna
-- * Query principal del reporte

SELECT *
FROM usuarios u
-- // WHERE activo = 1  -- Ya no se usa este filtro
WHERE estado = 'ACTIVO'; -- REVIEW: Validar estados posibles
