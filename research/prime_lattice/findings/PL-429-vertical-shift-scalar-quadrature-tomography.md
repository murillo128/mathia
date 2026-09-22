# PL-429 — Vertical-shift scalar response recovers the coherence hidden from same-shift L-products

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-HARMONIC-ANALYSIS + REPRESENTATION-ESCAPE + ANALYTIC-TRANSFER-BOUNDARY`.

**Parent findings:** `PL-421`, `PL-427`, `PL-428`.

## Claim

`PL-428` proves that scalar variances of ordinary products

\[
\prod_j L(s,\chi_j)^{m_j},\qquad m_j\in\mathbb N_0,
\]

cannot see the three imaginary mod-5 character coherences needed by the `PL-421` matrix cone test: every such logarithmic derivative uses a real coefficient vector in character space. That obstruction is exact for **same-shift products**, but it is not intrinsic to scalar variance once the canonical vertical flow is allowed.

Let `T` be any finite linear arithmetic-window operator and let `a=(a_n)`, `b=(b_n)` be finitely supported coefficient sequences with support in `n>=2`. Put

\[
U:=Ta,
\qquad
V_t:=T(b_n n^{-it})_{n\ge2},
\]

in the Hilbert space in which the scalar variance is measured, and define

\[
C_{a,b}(t):=\langle U,V_t\rangle.
\tag{1}
\]

Then `C_(a,b)` is a finite exponential polynomial with **only positive log-frequencies**:

\[
\boxed{
C_{a,b}(t)=\sum_{n\ge2}\beta_n e^{it\log n}.
}
\tag{2}
\]

The scalar polarization response

\[
R_{a,b}(t)
:=
\|U+V_t\|^2-\|U\|^2-\|V_t\|^2
\tag{3}
\]

therefore satisfies

\[
\boxed{
R_{a,b}(t)=2\Re C_{a,b}(t)
=C_{a,b}(t)+\overline{C_{a,b}(t)}.
}
\tag{4}
\]

Because the two terms in (4) occupy disjoint positive and negative frequency sets, positive-frequency projection recovers the full complex cross response exactly:

\[
\boxed{
C_{a,b}=P_+R_{a,b}.
}
\tag{5}
\]

Equivalently, in Fourier-Bohr coefficients,

\[
\boxed{
\beta_n
=
\mathsf M_t\!\left(
R_{a,b}(t)e^{-it\log n}
\right),
}
\tag{6}
\]

where `M_t` is the Bohr mean. In particular the formerly invisible quadrature at zero shift is determined by the **real scalar variance response as a function of vertical shift**. With the standard Hilbert-transform convention

\[
(Hf)(x)=\frac1\pi\operatorname{PV}\int_{\mathbb R}\frac{f(t)}{x-t}\,dt,
\]

one has for the finite exponential polynomial

\[
\boxed{
\Re C_{a,b}(0)=\frac12R_{a,b}(0),
\qquad
\Im C_{a,b}(0)=\frac12(HR_{a,b})(0)
=-\frac1{2\pi}
\operatorname{PV}\int_{\mathbb R}\frac{R_{a,b}(t)}t\,dt.
}
\tag{7}
\]

Thus the three imaginary coherences isolated in `PL-428` are not lost by scalarization if scalar data are retained along the vertical-shift parameter. They become phase-quadrature data of the one-sided `log n` spectrum.

For Dirichlet logarithmic derivatives this is not an artificial modulation. If

\[
a_n=\Lambda(n)\chi_j(n)w_n,
\qquad
b_n=\Lambda(n)\chi_k(n)w_n,
\]

then multiplication of the second coefficient sequence by `n^{-it}` is exactly the coefficient change induced by

\[
-\frac{L'}{L}(s+it,\chi_k)
=
\sum_{n\ge1}\frac{\Lambda(n)\chi_k(n)n^{-it}}{n^s}
\qquad(\Re s>1),
\tag{8}
\]

and the combined scalar channel is the logarithmic derivative of the legitimate shifted product

\[
L(s,\chi_j)L(s+it,\chi_k).
\tag{9}
\]

No complex powers of an L-function are required. In exponent coordinates the same phase is

\[
n^{-it}
=
\exp\!\left(-it\langle v(n),(\log p)_p\rangle\right),
\tag{10}
\]

so the tomography uses precisely the Kronecker/Bohr flow singled out by the prime-exponent lattice.

This is a **representation-level escape only**. It does not provide the unconditional, weaker-than-RH analytic estimate needed by `PL-421`. A useful theorem would now have to control the scalar shifted-product response `R_(a,b)(t)` with enough uniformity in `t` that the positive-frequency/Hilbert reconstruction remains quantitatively stable. Existing same-channel or GRH-conditional variance results do not supply that input automatically.

## 1. Exact one-sided frequency decomposition

Write the window operator abstractly as

\[
(Tc)(y)=\sum_n c_n K_y(n),
\tag{11}
\]

where only finitely many `n` occur. Then, with the Hilbert inner product linear in the first argument,

\[
\begin{aligned}
C_{a,b}(t)
&=
\int
\left(\sum_m a_mK_y(m)\right)
\overline{
\left(\sum_n b_n n^{-it}K_y(n)\right)
}
\,dy\\
&=
\sum_n
\left[
\overline{b_n}
\sum_m a_m
\int K_y(m)\overline{K_y(n)}\,dy
\right]
e^{it\log n}.
\end{aligned}
\tag{12}
\]

The bracketed expression is `beta_n`, proving (2). Since `n>=2`, every frequency `log n` is strictly positive. Unique factorization is not needed for the positivity itself, but in prime-lattice coordinates each frequency is the exact energy

\[
\log n=\langle v(n),(\log p)_p\rangle.
\tag{13}
\]

Expanding the norm in (3) gives (4). The conjugate term has frequencies `-log n`; hence its positive-frequency projection vanishes, while `P_+ C_(a,b)=C_(a,b)`. This proves (5).

Taking the Bohr mean of (4) against `e^{-it log n}` proves (6), because distinct integers have distinct `log n`. There is no zero-frequency ambiguity because the von-Mangoldt/prime source has no `n=1` coefficient.

## 2. Direct quadrature formula

For one term `beta e^{i omega t}`, `omega>0`,

\[
2\Re(\beta e^{i\omega t})
=2\Re\beta\cos(\omega t)-2\Im\beta\sin(\omega t).
\tag{14}
\]

The symmetric principal-value identities

\[
\operatorname{PV}\int_{-\infty}^{\infty}
\frac{\cos(\omega t)}t\,dt=0,
\qquad
\operatorname{PV}\int_{-\infty}^{\infty}
\frac{\sin(\omega t)}t\,dt=\pi
\quad(\omega>0)
\tag{15}
\]

then give

\[
-\frac1{2\pi}
\operatorname{PV}\int_{\mathbb R}
\frac{2\Re(\beta e^{i\omega t})}{t}\,dt
=
\Im\beta.
\tag{16}
\]

Summing the finitely many terms proves the imaginary-part identity in (7). This is the ordinary analytic-signal/Hilbert-transform relation: a one-sided spectrum is determined by its real boundary trace. No novelty is claimed for that harmonic-analysis fact.

The important line-specific point is that the one-sided frequencies here are not introduced by hand. They are exactly the arithmetic energies `log n`, and the modulation parameter is exactly vertical translation of the Dirichlet L-channel.

## 3. Consequence for the mod-5 blind sector

Let `A_j` and `A_k` denote two character channels in the notation of `PL-428`, with mixed covariance

\[
K_{jk}=\langle A_j,A_k\rangle.
\tag{17}
\]

At zero shift, `C_(j,k)(0)=K_(jk)`. Same-shift ordinary products determine only

\[
\Re K_{jk}
=\frac12R_{j,k}(0),
\tag{18}
\]

which is exactly the loss proved in `PL-428`. But the full vertical-shift response gives

\[
\boxed{
K_{jk}
=
\frac12R_{j,k}(0)
-
\frac{i}{2\pi}
\operatorname{PV}\int_{\mathbb R}
\frac{R_{j,k}(t)}t\,dt.
}
\tag{19}
\]

Hence the three coordinates

\[
\Im K_{01},\qquad
\Im K_{21},\qquad
\Im K_{13}
\tag{20}
\]

are all scalar-recoverable once the scalar probe family includes vertical shifts. The `PL-428` matched controls remain indistinguishable to every same-shift real product variance, but they cannot remain indistinguishable to the complete function `t -> R_(j,k)(t)` unless their hidden coherences are actually equal.

This changes the representation frontier. The remaining obstruction is no longer “scalar observables cannot encode the missing phase.” It is:

\[
\boxed{
\text{can arithmetic analysis control the required vertical-shift scalar response
strongly enough to reconstruct the phase without assuming RH/GRH?}
}
\tag{21}
\]

## 4. Relation to current variance and zero-correlation routes

`PL-427` shows that the Kandhil--Languasco--Moree proof becomes matrix-complete under arbitrary complex polarization, but only under GRH. `PL-428` then shows that ordinary same-shift L-products cannot manufacture those complex coefficient vectors by integer multiplicities.

The present construction provides a third option: do not use complex powers and do not require a complex coefficient vector inserted by fiat. Use the canonical vertical translation already present in Dirichlet-series dynamics. On the prime side it inserts the phase `n^{-it}`; on the exponent lattice it is the character generated by the energy `log n`; on the scalar variance side the whole `t`-response is an analytic signal whose quadrature recovers the missing complex coherence.

This does **not** imply that the Bui--Keating--Smith theorem or the KLM theorem can simply be applied to (9). The former is calibrated in `PL-428` as a primitive Selberg-class theorem, whereas products of shifted factors are generally not primitive. The latter uses GRH, including the principal mod-5 channel and therefore RH for zeta. A new analytic estimate is still required.

Nor is pointwise control at a few shifts enough in general. Formula (19) is global in the shift variable, and the Fourier-Bohr reconstruction (6) separates frequencies that can be arbitrarily close at large `n`. Approximate data with weak or nonuniform errors can therefore be badly conditioned. The exact tomography removes an information-theoretic obstruction; it does not remove the quantitative analytic one.

## 5. Prior-art and novelty audit

The ingredients are classical.

- Bohr's theory identifies vertical Dirichlet polynomials as almost-periodic exponential polynomials with frequencies `log n`; the Hedenmalm--Lindqvist--Seip framework already registered in `SOURCES.md` is the line's standard modern anchor for these vertical characters.
- Positive-frequency projection and the Hilbert-transform relation between the real and imaginary parts of a one-sided spectrum are classical Hardy-space/analytic-signal facts (Titchmarsh/Paley--Wiener theory).
- Vertical translation of a Dirichlet L-function gives the coefficient multiplier `n^{-it}` by direct substitution in its absolutely convergent logarithmic derivative for `Re(s)>1`.

Targeted searches did not locate a source making the specific `PL-428` connection: namely, that scalar variances of vertically shifted Dirichlet-L products form an exact quadrature-tomography family for the three mod-5 imaginary coherences that same-shift ordinary products provably miss. No novelty is claimed for almost periodicity, the Hilbert transform, scalar polarization, or vertical shifts separately.

The durable contribution is therefore a **frontier correction/escape** internal to this line: the same-shift scalar blind sector of `PL-428` is not invariant under the canonical `log n` flow. The prime-exponent dynamics themselves provide an exact phase-quadrature carrier, but exploiting it for RH still requires new arithmetic control rather than more finite-dimensional algebra.

## 6. Adversarial audit and failure modes

1. **No RH consequence is claimed.** Exact reconstructibility of `K_(jk)` from ideal shifted scalar data is not an estimate for the actual prime covariance and does not prove the `1/4` spectral floor of `PL-421`.
2. **The reconstruction needs the shift response, not one scalar theorem.** Same-shift data at `t=0` retain exactly the blindness of `PL-428`.
3. **Approximate inversion may be unstable.** Recovering positive-frequency data from asymptotic scalar estimates requires uniform error control in `t`; formula (19) is a principal-value/global statement and cannot be fed an uncontrolled `o(1)` pointwise error.
4. **The shifted product is not asserted to be primitive.** Equation (9) is a legitimate meromorphic product, but existing primitive-Selberg-class variance theorems cannot be imported without checking their hypotheses.
5. **GRH-based shifted estimates remain circular.** The principal mod-5 factor contains zeta, so a result whose proof assumes GRH has no proof-level value for RH even if it supplies perfect tomography.
6. **The derivation is finite/truncated.** For infinite coefficient systems one needs the appropriate almost-periodic/Hardy convergence before using `P_+` or the Hilbert transform. The finite prime-window statistics relevant to covariance transfer already satisfy the exact algebra above.
7. **A zero-frequency coefficient would be exceptional.** A term at `n=1` would contribute a constant whose imaginary part cannot be recovered from its real trace. The von-Mangoldt source has no such term, so this does not affect the intended application.
8. **Centering must be transported consistently.** Deterministic centering terms are linear and can be included or subtracted before (3); the identity does not justify replacing a shifted center by an unshifted one.

## Consequence

Do not generalize the `PL-428` obstruction from same-shift ordinary L-products to all scalar L-function probes. The canonical vertical flow already restores representation completeness: the hidden imaginary coherence is the Hilbert-transform quadrature of a scalar shifted-product response.

The viable continuation is correspondingly sharper. Search for an unconditional or genuinely weaker-than-RH estimate for the scalar family generated by

\[
L(s,\chi_j)L(s+it,\chi_k)
\]

(or an equivalent prime-side vertically modulated statistic) that is sufficiently uniform in `t` to survive the positive-frequency reconstruction and imply the `PL-421` matrix floor. If such control cannot be obtained without reintroducing GRH, the route closes analytically rather than algebraically.