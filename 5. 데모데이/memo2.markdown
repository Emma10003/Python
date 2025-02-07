<변수 선택법>

- Lasso 기법

from sklearn.linear_model import LassoCV

# Lasso로 특성 선택 (Lasso는 L1 정규화를 사용하여 불필요한 변수 제거)
lasso = LassoCV(cv=5)
lasso.fit(X_train_scaled, y_train)

# 중요하지 않은 특성의 계수는 0으로 설정되므로, 이를 통해 특성 선택
selected_features = np.where(lasso.coef_ != 0)[0]
X_train_selected = X_train_scaled[:, selected_features]
X_valid_selected = X_valid_scaled[:, selected_features]

# 모델 학습
model.fit(X_train_selected, y_train)
y_pred = model.predict(X_valid_selected)
mae = mean_absolute_error(y_valid, y_pred)
print(f"Validation MAE with selected features: {mae}")

=================================================================
L1 정규화(Lasso Regression) -> 정규화 성능이 좀 떨어지는 대신 이상치 민감성 낮음
L2 정규화(Ridge Regression) -> 정규화 효과는 좋은데 이상치 민감성 높음
=================================================================
교차 검증 (Cross Validation)

from sklearn.model_selection import cross_val_score

# 교차 검증으로 성능 평가
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='neg_mean_absolute_error')
print(f"Cross-validation MAE: {np.mean(cv_scores)} ± {np.std(cv_scores)}")
