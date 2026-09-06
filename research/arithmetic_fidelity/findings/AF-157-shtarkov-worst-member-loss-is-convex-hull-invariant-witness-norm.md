# AF-157 — Shtarkov worst-member loss is a convex-hull-invariant likelihood-witness norm

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `POSITIVE-REFERENCE-CONSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-154 identifies the full Shtarkov likelihood-ray loss with the squared-error Bayes risk for reconstructing the entire max-normalized likelihood vector, while AF-156 shows that summing all coordinate losses is not uniformly calibrated to whole-experiment recovery as the family grows. The missing distinction is not merely a normalization constant: the raw sum uses the parameter list itself as an unweighted Euclidean coordinate system, so it can change under mathematically harmless duplication or redundant convex enrichment of that list.

There is a source-natural aggregation that removes that representation dependence for a declared linear likelihood-witness class.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite sample space `X`. Define its Shtarkov envelope, mass, and reference by

\[
s(x)=\max_iP_i(x),
\qquad
C=\sum_xs(x),
\qquad
M(x)=\frac{s(x)}C.
\tag{1}
\]

For a stochastic compression

\[
K:X\rightsquigarrow Y,
\]

put `q=MK` and use the max-normalized source likelihood coordinates

\[
U_i(x)=\frac{P_i(x)}{s(x)}.
\tag{2}
\]

Under the reference joint law `M(x)K(y|x)`, let

\[
r_i(X,Y)
:=U_i(X)-\mathbb E_M[U_i(X)\mid Y].
\tag{3}
\]

AF-154 gives the individual Shtarkov-reference Pearson losses

\[
\varepsilon_i^*(K)
:=
\chi^2(P_i\|M)-\chi^2(P_iK\|q)
=C^2\|r_i\|_{L^2(MK)}^2.
\tag{4}
\]

Define the **convex-hull Shtarkov defect**

\[
\boxed{
\Gamma_{\rm Sh}(K;\mathcal E)
:=\max_i\varepsilon_i^*(K).
}
\tag{5}
\]

Then:

1. for every signed coefficient vector `a in R^m`, the irreducible squared-error loss of the linear likelihood witness
   \[
   U_a:=\sum_i a_iU_i
   \]
   after observing only `Y` is
   \[
   \inf_g\mathbb E_M[(U_a-g(Y))^2]
   =\left\|\sum_i a_ir_i\right\|_2^2;
   \tag{6}
   \]
2. the worst loss over the `ell_1` unit ball is exactly the worst individual Pearson loss:
   \[
   \boxed{
   \sup_{\|a\|_1\le1}
   \inf_g\mathbb E_M[(U_a-g(Y))^2]
   =
   \frac{\Gamma_{\rm Sh}(K;\mathcal E)}{C^2};
   }
   \tag{7}
   \]
   equivalently, if
   \[
   \mathsf R_K:a\mapsto\sum_i a_ir_i,
   \]
   then
   \[
   \boxed{
   \Gamma_{\rm Sh}
   =C^2\|\mathsf R_K\|_{\ell_1^m\to L^2(MK)}^2;
   }
   \tag{8}
   \]
3. restricting `(7)` to probability mixtures does not change the supremum. If
   \[
   P_\lambda=\sum_i\lambda_iP_i,
   \qquad \lambda\in\Delta_m,
   \]
   and
   \[
   \varepsilon^*(P_\lambda;K)
   :=\chi^2(P_\lambda\|M)-\chi^2(P_\lambda K\|q),
   \]
   then
   \[
   \boxed{
   \sup_{\lambda\in\Delta_m}
   \varepsilon^*(P_\lambda;K)
   =\max_i\varepsilon_i^*(K)
   =\Gamma_{\rm Sh};
   }
   \tag{9}
   \]
4. consequently `Gamma_Sh` depends only on the convex hull
   \[
   \operatorname{conv}\{P_1,\ldots,P_m\}
   \]
   and on `K`. Replacing the parameter list by any other finite generating family with the same convex hull — in particular duplicating a member or adjoining arbitrary redundant mixtures — leaves `s`, `C`, `M`, and `Gamma_Sh` unchanged;
5. the target recovery notion has the same harmless-reparameterization invariance:
   \[
   \boxed{
   \delta_{\rm rec}(K;\mathcal E)
   =
   \delta_{\rm rec}
   \left(K;\operatorname{conv}(\mathcal E)\right);
   }
   \tag{10}
   \]
6. the Shtarkov Bayes reverse from AF-149 therefore gives the dimension-free one-way recovery certificate
   \[
   \boxed{
   4\,\delta_{\rm rec}(K;\mathcal E)^2
   \le
   \Gamma_{\rm Sh}(K;\mathcal E);
   }
   \tag{11}
   \]
7. its exact zero set is still complete:
   \[
   \boxed{
   \Gamma_{\rm Sh}=0
   \iff
   K\text{ is sufficient for }\mathcal E.
   }
   \tag{12}
   \]

This separates two natural operator geometries on the same Shtarkov likelihood-ray representation. AF-154's normalized full-ray risk is

\[
R_{\rm ray}
=\sum_i\|r_i\|_2^2,
\tag{13}
\]

which is the squared Hilbert--Schmidt norm of the residual operator when the listed parameter coordinates are given an unweighted Euclidean structure. By contrast, `(7)` is its squared `ell_1 -> L^2` operator norm. The first asks to reconstruct **all listed coordinates simultaneously** and therefore counts coordinate multiplicity; the second asks for the worst bounded linear witness and is unchanged by redundant convex reparameterization.

Thus AF-156's failure of raw likelihood-ray aggregation does not imply that the Shtarkov representation itself lacks a complexity-stable destination calibration. For the bounded linear/mixture witness class, `Gamma_Sh` is canonical at the level of the experiment's convex hull and still controls one common recovery kernel. It is not, however, a two-sided metric equivalent to Le Cam deficiency.

## Derivation

### Conditional expectation gives every linear-witness risk

For any `a in R^m`, linearity of conditional expectation gives

\[
\mathbb E[U_a\mid Y]
=\sum_i a_i\mathbb E[U_i\mid Y].
\]

Therefore

\[
U_a-\mathbb E[U_a\mid Y]
=\sum_i a_ir_i.
\tag{14}
\]

The classical `L^2` projection property of conditional expectation makes the conditional mean the unique minimum-square predictor, proving `(6)`.

Now use the triangle inequality in `L^2`:

\[
\left\|\sum_i a_ir_i\right\|_2
\le
\sum_i|a_i|\,\|r_i\|_2
\le
\|a\|_1\max_i\|r_i\|_2.
\tag{15}
\]

Hence the left side of `(7)` is at most `max_i ||r_i||_2^2`. Equality is attained by taking `a=e_j` for an index `j` with maximal residual norm. Multiplying by `C^2` and using `(4)` proves `(7)--(8)`.

Equivalently, if

\[
\Sigma_K
:=\mathbb E[r\,r^\top]
\succeq0,
\qquad
r=(r_1,\ldots,r_m),
\tag{16}
\]

then

\[
\|\mathsf R_K a\|_2^2=a^\top\Sigma_Ka,
\]

and `(7)` says

\[
\sup_{\|a\|_1\le1}a^\top\Sigma_Ka
=\max_i(\Sigma_K)_{ii}.
\tag{17}
\]

No covariance cancellation is being assumed: `(15)` proves the result directly for every positive-semidefinite residual covariance.

### Mixture witnesses and the convex hull

For `lambda in Delta_m`, define

\[
P_\lambda=\sum_i\lambda_iP_i.
\]

Because the Shtarkov envelope `s` is fixed by the source experiment,

\[
U_\lambda
:=\frac{P_\lambda}{s}
=\sum_i\lambda_iU_i.
\tag{18}
\]

Moreover

\[
\frac{P_\lambda}{M}=C U_\lambda,
\qquad
\frac{P_\lambda K}{q}
=C\,\mathbb E[U_\lambda\mid Y].
\tag{19}
\]

The same conditional-variance calculation used in AF-154 therefore gives

\[
\varepsilon^*(P_\lambda;K)
=C^2
\left\|\sum_i\lambda_ir_i\right\|_2^2.
\tag{20}
\]

Applying `(15)` with `lambda_i>=0` and `sum_i lambda_i=1` shows

\[
\varepsilon^*(P_\lambda;K)
\le\max_i\varepsilon_i^*(K),
\]

while the simplex contains every vertex `e_i`. This proves `(9)`.

Now suppose another finite family `E'` has exactly the same convex hull as `E`. For every sample point `x`, evaluation `P -> P(x)` is linear, so

\[
\sup_{P\in\operatorname{conv}(\mathcal E)}P(x)
=\max_iP_i(x).
\tag{21}
\]

Hence equal convex hulls have the same pointwise envelope `s`, and therefore the same `C` and Shtarkov reference `M`. Equation `(9)` then identifies `Gamma_Sh` as the supremum of one fixed quadratic loss over that common convex set, so it too is unchanged. This proves the claimed reparameterization invariance.

### Recovery deficiency is also convex-hull invariant

Fix any reverse channel `R:Y -> X`. For a mixture `P_lambda`, linearity of channels and convexity of total variation give

\[
\begin{aligned}
\|P_\lambda-P_\lambda K R\|_{\rm TV}
&=
\left\|
\sum_i\lambda_i(P_i-P_iKR)
\right\|_{\rm TV}\\
&\le
\sum_i\lambda_i
\|P_i-P_iKR\|_{\rm TV}\\
&\le
\max_i\|P_i-P_iKR\|_{\rm TV}.
\end{aligned}
\tag{22}
\]

The original members are themselves in the convex hull, so the supremum over the hull equals the maximum over the original family for every fixed `R`. Taking the infimum over `R` proves `(10)`.

AF-149 supplies one particular reverse, the Bayes reverse generated by the source Shtarkov reference, for which

\[
4\|P_i-P_iKR_M\|_{\rm TV}^2
\le\varepsilon_i^*(K)
\]

simultaneously for every member. Maximizing over `i` and then using the definition of deficiency proves `(11)`.

Finally, `Gamma_Sh=0` exactly when every individual residual `r_i` vanishes. That is equivalent to AF-154's full sum

\[
\sum_i\varepsilon_i^*=0,
\]

whose zero set is exactly finite-experiment sufficiency. This proves `(12)`.

## Why the raw likelihood-ray trace fails harmless-reparameterization

The distinction from AF-154's full-ray quantity is exact rather than asymptotic. If a model `P_j` is listed twice, the pointwise envelope, Shtarkov reference, experiment convex hull, deficiency, and `Gamma_Sh` are unchanged. But `(13)` acquires one extra copy of

\[
\|r_j\|_2^2.
\]

Repeating the same parameter label arbitrarily many times can therefore make the raw trace arbitrarily large whenever that coordinate has nonzero loss, without changing the underlying statistical experiment at all.

This does not invalidate `R_ray` for the explicitly declared Euclidean vector-reconstruction task. It shows that the Euclidean coordinate measure is extra destination structure. If the intended object is the statistical experiment only up to redundant parameterization, the trace is not intrinsic until a justified measure or geometry on parameter space is supplied.

## Exact arithmetic/analytic stress test: the local `p=2` Euler-factor family

AF-154 already supplies a two-member arithmetic/analytic control from one ordinary rational prime. On exponents `k=1,2,3`, take the normalized local profiles

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right),
\tag{23}
\]

and let `K` retain `k=1` while merging `k=2,3`. Their Shtarkov data are

\[
s=\left(\frac{16}{21},\frac27,\frac17\right),
\qquad
C=\frac{25}{21},
\qquad
M=\left(\frac{16}{25},\frac6{25},\frac3{25}\right).
\tag{24}
\]

The max-normalized likelihood rays are

\[
U_1=\left(\frac34,1,1\right),
\qquad
U_2=\left(1,\frac23,\frac13\right).
\tag{25}
\]

The first coordinate is constant on the merged fiber, so

\[
\varepsilon_1^*=0.
\]

For the second coordinate, the conditional mean on the merged fiber is `5/9`, giving

\[
\mathbb E[r_2^2]=\frac{2}{225}
\]

and therefore

\[
\boxed{
\varepsilon_2^*
=C^2\frac{2}{225}
=\frac{50}{3969}.
}
\tag{26}
\]

Thus

\[
\Gamma_{\rm Sh}=\frac{50}{3969}.
\tag{27}
\]

Adjoin the redundant mixture

\[
P_{1/2}=\frac12(P_1+P_2).
\]

It cannot change the pointwise envelope because it lies in the convex hull. Its exact loss is

\[
\varepsilon^*(P_{1/2};K)
=\frac{25}{7938}
<\Gamma_{\rm Sh},
\tag{28}
\]

so the profile stays unchanged as `(9)` predicts. Likewise, duplicating `P_2` leaves `Gamma_Sh` equal to `(27)`, while AF-154's raw sum of coordinate losses doubles from `50/3969` to `100/3969`. The same arithmetic compression therefore distinguishes intrinsic convex-hull calibration from parameter-list-dependent Euclidean aggregation without invoking a generalized-prime control.

## AF-156 private-label stress test and the remaining boundary

For AF-156's private-label family,

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\]

one has

\[
\delta_m=\rho\left(1-\frac1m\right),
\qquad
C_m=1+(m-1)\rho,
\]

and every individual Shtarkov Pearson loss is the same:

\[
\boxed{
\Gamma_{\rm Sh}
=C_m\delta_m.
}
\tag{29}
\]

If

\[
\rho_m=m^{-\alpha},
\qquad
\frac12<\alpha<1,
\]

then AF-156 gives

\[
\delta_m\to0,
\qquad
\Gamma_{\rm Sh}\sim m^{1-2\alpha}\to0,
\]

while the raw full-ray and radial aggregate risks tend to one. Thus the convex-hull/operator-norm aggregation survives that specific family-size obstruction as a vanishing one-way certificate.

But it is still not uniformly equivalent to deficiency. At the boundary scale

\[
\rho_m=m^{-1/2},
\]

one has

\[
\delta_m\sim m^{-1/2}\to0,
\qquad
\Gamma_{\rm Sh}	o1.
\tag{30}
\]

Therefore no dimension-free converse of the form

\[
\Gamma_{\rm Sh}\le f(\delta_{\rm rec}),
\qquad f(t)\to0,
\]

can hold over all finite experiments. The result calibrates the Shtarkov representation to one explicit destination witness class; it does not solve the stronger problem of finding a two-sided recovery geometry uniform over growing experiment complexity.

## Prior art and novelty assessment

The ingredients are classical. Conditional expectation as orthogonal projection in `L^2`, and the resulting conditional-variance/Pythagorean identity, are standard probability and Rao--Blackwell theory; AF-009 already audits this against Blackwell and Kallenberg. Shtarkov's normalized maximum-likelihood envelope and minimax-regret interpretation are classical and are already audited in AF-149. Comparison and recovery of statistical experiments are classical Blackwell/Le Cam/Torgersen territory, while AF-144/AF-149 already supply the common-reference Pearson recovery inequality used in `(11)`.

Targeted literature searches for Shtarkov/NML combined with convex-hull invariance, Pearson data-processing loss, and statistical-experiment deficiency did not establish this exact package as a standard named theorem. That absence is not evidence of novelty. Equations `(7)--(12)` are elementary consequences of the classical `L^2` projection identity, convexity, the Shtarkov source reference, and the already-audited recovery bound. The durable contribution here is the **calibration and falsification distinction** relevant to Arithmetic Fidelity: the worst-member Shtarkov loss is exactly the operator norm for a convex-hull-invariant likelihood-witness class, whereas the raw likelihood-ray trace can be changed arbitrarily by redundant parameter labels.

## Consequence for the line

The current Shtarkov branch now has a principled answer for one part of the destination-calibration problem. A source-selected likelihood-ray representation can be paired with a destination witness geometry that is invariant under harmless convex reparameterization and whose constants do not explicitly grow with the number of listed models. The right aggregation is determined by the declared witness class: simultaneous Euclidean vector reconstruction yields a trace, while bounded linear/mixture witnesses yield an operator norm.

The remaining frontier is sharper. For a concrete downstream theorem — eventually including rational-prime versus matched-control discrimination — one should first identify its actual admissible witness/decision class and then derive the corresponding norm or risk on the retained likelihood structure. A useful next theorem would need either a two-sided complexity-uniform recovery modulus for such a class or an exact obstruction proving that the endpoint necessarily consumes information outside every source-natural bounded witness geometry of this type.