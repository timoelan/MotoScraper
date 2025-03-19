import React, { useEffect, useState } from 'react';
import { getTuttiContent } from '../services/api';
import { Card, CardContent, CardMedia, Typography, Grid, Container, TextField } from '@mui/material';
import { Link } from 'react-router-dom';
import './MotorradList.css';
import { Motorrad } from './Motorrad';

const MotorradList: React.FC = () => {
  const [tuttiData, setTuttiData] = useState<Motorrad[]>([]);
  const [searchTerm, setSearchTerm] = useState<string>('');

  useEffect(() => {
    const fetchData = async () => {
      const tuttiContent = await getTuttiContent();
      setTuttiData(tuttiContent);
    };

    fetchData();
  }, []);

  const filteredData = tuttiData.filter((motorrad) =>
    motorrad.Titel.toLowerCase().includes(searchTerm.toLowerCase()) 
  );

  return (
    <Container className="motorrad-list-container">
      <Typography variant="h4" className="page-title" gutterBottom>
        Tutti Motorräder
      </Typography>

      <TextField
        label="Suche nach Titel"
        variant="outlined"
        fullWidth
        margin="normal"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)} 
      />

      <Grid container spacing={4}>
        {filteredData.map((motorrad) => (
          <Grid item key={motorrad.id} xs={12} sm={6} md={4}>
            <Link to={`/motorrad/${motorrad.id}`} style={{ textDecoration: 'none' }}>
              <Card className="motorrad-card">
                <CardMedia
                  component="img"
                  className="motorrad-image"
                  image={motorrad["Bild-URL"]}
                  alt={motorrad.Titel}
                />
                <CardContent>
                  <Typography className="motorrad-title" gutterBottom variant="h5" component="div">
                    {motorrad.Titel}
                  </Typography>
                  <Typography className="motorrad-price">
                    {motorrad.Preis}
                  </Typography>
                  <Typography className="motorrad-location">
                    {motorrad.Ort}
                  </Typography>
                  <Typography className="motorrad-description" variant="body2" color="text.secondary">
                    {motorrad.Beschreibung.substring(0, 100)}...
                  </Typography>
                  <Typography className="motorrad-add-time" variant="body2" color="primary">
                    {motorrad['Hinzugefügt am']}
                  </Typography>
                </CardContent>
              </Card>
            </Link>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default MotorradList;