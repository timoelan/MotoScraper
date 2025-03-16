import React, { useEffect, useState } from 'react';
import { getTuttiContent } from '../services/api';
import { Card, CardContent, CardMedia, Typography, Grid, Container } from '@mui/material';
import { Link } from 'react-router-dom';
import './MotorradList.css';
import { Motorrad } from './Motorrad';

const MotorradList: React.FC = () => {
  const [tuttiData, setTuttiData] = useState<Motorrad[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const tuttiContent = await getTuttiContent();
      setTuttiData(tuttiContent);
    };

    fetchData();
  }, []);

  return (
    <Container className="motorrad-list-container">
      <Typography variant="h4" className="page-title" gutterBottom>
        Tutti Motorräder
      </Typography>
      <Grid container spacing={4}>
        {tuttiData.map((motorrad) => (
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