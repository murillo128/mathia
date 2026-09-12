# MI-001 — Farey occupation has a deterministic critical host and a below-critical localization barrier

**Evidence level:** supported by exact source/occupation reductions through FD-059; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

Signed multiplicative rays are not coercive, while quadratic occupation admits an additive twin mechanism. FD-054--FD-058 separated deterministic transfer, strong short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization.

FD-059 identifies the natural host scale sharply. Put `A_X=|\mathcal H(X)|` and `Q_X=X/A_X`. For every fixed `lambda>1`, a squarefree host `q=3 mod 4` can be selected with `q asymp lambda Q_X`; then `q+1` is nonsquarefree and the associated quotient point satisfies

\[
|\mathcal H(x^*)|\ge (1-1/\lambda)A_X-1.
\]

Therefore a comparable nonsquarefree quadratic contribution is forced at `q asymp X/A_X` with no short-interval theorem. Along a false-RH spike `A_X=X^{\Theta+o(1)}`, this reaches the critical row exponent

\[
\alpha_\Theta=\frac{1-\Theta}{2-\Theta}
\]

for every `\Theta>1/2`. Taking a subpower `lambda_X -> infinity` gives first-order transfer while retaining the same power exponent.

Thus the condition `qA_X/X -> infinity` from the earlier arbitrary-host transfer is the threshold for relative error `o(1)`, not the threshold for useful positive-fraction quadratic energy when a favorable host may be selected.

The maximal-localization program becomes load-bearing only **below** the natural scale: `q=o(X/A_X)`, equivalently transfer lengths `R_X=A_XL_X` with `L_X -> infinity`. There bounded increments no longer prevent complete cancellation, so genuine short-interval/maximal source control or another source-coupled mechanism is needed.

**Boundary.** A single comparable nonsquarefree row does not imply a fixed lower bound for the global ratio `U/E`; unrelated low rows may dominate. FD-059 relocates the source-regularity threshold but does not solve global occupation.
