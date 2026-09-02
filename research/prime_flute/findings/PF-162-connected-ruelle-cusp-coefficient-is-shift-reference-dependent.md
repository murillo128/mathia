# PF-162 — connected Ruelle cusp coefficient is shift-reference dependent

**Status:** `EXACT-DERIVED + CLASSICAL-INPUT + LITERATURE-AUDITED + DECISIVE-NEGATIVE/REFERENCE-DEPENDENCE`. PF-161 shows that, for the exact all-composite control `p -> p+1`, the connected canonical bottom-Ruelle product has a finite nonzero value at `s=0` but a logarithmic-derivative cusp

\[
\frac d{ds}\log \mathcal R_{0,1}(s)
\sim C_1\log\frac1s.
\]

The present finding stress-tests whether the coefficient `C_1` can carry intrinsic prime-flute arithmetic. It cannot. There is a natural infinite family of exact all-composite controls obtained by any fixed **positive odd shift** `m`: the labels `p+m` are all even composite, their pre-cotangent gap pattern is exactly the prime gap pattern, and after the canonical translation normalization their sampled endpoint defect still tends to zero and is `ell^1`. Repeating the PF-159--PF-161 connected canonical construction gives a cusp coefficient `C_m`, but

\[
\boxed{
C_m=\frac{2\pi^2}{3}\log\log m+O(1)
\qquad(m\to\infty,\ m\ \text{odd}).
}
\]

In particular `C_m` is unbounded across exact all-composite references. The nonzero `s log(1/s)` cusp of the selected connected bottom-Ruelle sector is therefore **not an intrinsic invariant of the prime flute and not a prime-gap/RH selector**. It is a relative-reference effect whose magnitude can be changed arbitrarily inside a canonical matched-control family.

This does **not** compare full Ruelle zeta functions, full Selberg zeta functions, scattering matrices, resonances, or Laplace spectra for different `m`.

## 1. A canonical family of exact all-composite shift controls

Keep PF-106's exact endpoint law

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad x>2.
\tag{1}
\]

Fix a positive odd integer `m`. For every odd prime `p`,

\[
q=p+m
\tag{2}
\]

is even and at least `4`, hence composite. The sequence `q_n=p_n+m` is strictly increasing and has exactly the same consecutive label gaps as the prime sequence:

\[
q_{n+1}-q_n=p_{n+1}-p_n.
\tag{3}
\]

Feed the `q_n` through the same exact cotangent endpoint law and normalize by the hyperbolic translation `z -> z-m`. The resulting exact all-composite flute has endpoints

\[
\boxed{
W_m(x):=V(x+m)-m.
}
\tag{4}
\]

Define

\[
a(x):=x-V(x),
\qquad
\varepsilon_m(x):=W_m(x)-V(x).
\tag{5}
\]

Then

\[
\boxed{
\varepsilon_m(x)=a(x)-a(x+m)
=\int_x^{x+m}\bigl(V'(t)-1\bigr)\,dt.
}
\tag{6}
\]

PF-105/PF-106 give

\[
V'(x)=\left(\frac{\pi/x}{\sin(\pi/x)}\right)^2>1
\]

with `V'` strictly decreasing to `1`. Hence, for every fixed positive `m`,

\[
\varepsilon_m(x)>0,
\qquad
\varepsilon_m'(x)<0.
\tag{7}
\]

The cotangent expansion gives

\[
a(x)
=\frac{\pi^2}{3x}+O(x^{-3}),
\tag{8}
\]

and therefore, with constants allowed to depend on the fixed shift,

\[
\boxed{
\varepsilon_m(x)
=\frac{\pi^2m}{3x^2}+O_m(x^{-3}),
\qquad
\varepsilon_m'(x)=O_m(x^{-3}).
}
\tag{9}
\]

Consequently

\[
\sum_{p\ge3}\varepsilon_m(p)<\infty.
\tag{10}
\]

The same secant argument as PF-106 also gives an all-span tail comparison

\[
\left|\log\frac{\chi_m}{\chi}\right|=O_m(P^{-3})
\tag{11}
\]

for every matched four-endpoint cross-ratio whose leftmost label is at least `P`. Thus each fixed odd-shift control is asymptotically the same kind of exact sampled-endpoint perturbation as the `m=1` control. No uniformity in `m` is asserted.

## 2. The PF-159 one-ended decomposition is parameter-stable

Take a canonical PF-004 separator with consecutive exterior prime pairs

\[
a<b<c<d.
\tag{12}
\]

Write

\[
X=V(b)-V(a),\quad
Y=V(c)-V(b),\quad
Z=V(d)-V(c),\quad
S=X+Y+Z,
\]

\[
\chi=\frac{YS}{XZ},
\qquad
L=4\operatorname{arsinh}\sqrt\chi.
\tag{13}
\]

Put a superscript `(m)` on the corresponding quantities made from `W_m`. Since `\varepsilon_m` is strictly decreasing,

\[
X^{(m)}=X+\varepsilon_m(b)-\varepsilon_m(a)<X.
\tag{14}
\]

Define the exact left-edge response and one-ended model

\[
R_{a,m}:=\frac{X}{X^{(m)}}>1,
\qquad
\widehat\chi_m:=R_{a,m}\chi,
\qquad
\widehat L_m:=4\operatorname{arsinh}\sqrt{\widehat\chi_m}.
\tag{15}
\]

Exactly as in PF-159, but now with `\varepsilon_m`, there is the algebraic identity

\[
\boxed{
\frac{\chi^{(m)}}{R_{a,m}\chi}
=
\frac{Y^{(m)}}Y
\frac{S^{(m)}}S
\frac Z{Z^{(m)}}.
}
\tag{16}
\]

Fix the left pair `a<b` and send the right pair `c<d` through consecutive primes to infinity. Since `V(x)=x+O(x^{-1})`, consecutive prime gaps satisfy `d-c=o(c)` by the same BHP envelope already used in PF-158--PF-161, and (9) gives

\[
\boxed{
 c\log\frac{\chi^{(m)}}{\widehat\chi_m}
 \longrightarrow
 -\bigl(\varepsilon_m(a)+\varepsilon_m(b)\bigr).
}
\tag{17}
\]

Because the derivative of `4 asinh sqrt(u)` with respect to `log u` tends to `2` as `u -> infinity`, the corresponding exact length asymptotic is

\[
\boxed{
 c\bigl(L^{(m)}-\widehat L_m\bigr)
 \longrightarrow
 -2\bigl(\varepsilon_m(a)+\varepsilon_m(b)\bigr).
}
\tag{18}
\]

The proof uses only the structural properties `\varepsilon_m=O_m(x^-2)` and `\varepsilon_m'=O_m(x^-3)`. Hence the near/far summability estimates of PF-159 and PF-161 also carry over for every fixed `m`: in the far sector

\[
|L^{(m)}-\widehat L_m|
\le
C_m'\left(\frac{a^{-2}}c+c^{-3}\right),
\tag{19}
\]

while the near-span logarithmic length mismatch is `O_m(a^-3)`.

## 3. Every odd shift has the same logarithmic cusp mechanism

For real `s>0`, define the connected canonical bottom-Ruelle product for the `m`-shift reference by

\[
\boxed{
\mathcal R_{0,m}(s)
:=
\prod_{\eta\in\mathcal C}
\frac{1-e^{-sL_\eta^{(m)}}}
     {1-e^{-s\widehat L_{m,\eta}}}.
}
\tag{20}
\]

This is the same selected canonical bottom layer as PF-161, with the reference changed from `m=1` to the exact `m`-shift all-composite flute. Equations (9), (18), and (19) are precisely the inputs used in PF-161. Repeating that proof gives

\[
\sum_{\eta\in\mathcal C}
\left|\log\frac{L_\eta^{(m)}}{\widehat L_{m,\eta}}\right|<\infty,
\tag{21}
\]

so the product has a finite strictly positive real boundary value

\[
0<\mathcal R_{0,m}(0)<\infty.
\tag{22}
\]

For a left consecutive-prime pair `a<b`, put

\[
A_{a,m}:=\varepsilon_m(a)+\varepsilon_m(b)>0.
\tag{23}
\]

The fixed-left bottom-layer logarithmic derivative has the same Abelian prime-harmonic cutoff as PF-161, now with coefficient `A_{a,m}`. Summing over left gaps gives

\[
\boxed{
\frac d{ds}\log\mathcal R_{0,m}(s)
\sim C_m\log\frac1s,
\qquad
C_m:=\sum_a A_{a,m},
\qquad s\downarrow0.
}
\tag{24}
\]

Equivalently,

\[
\log\mathcal R_{0,m}(s)-\log\mathcal R_{0,m}(0)
\sim C_m s\log\frac1s.
\tag{25}
\]

Because consecutive odd-prime pairs overlap,

\[
\boxed{
C_m
=\varepsilon_m(3)
+2\sum_{p\ge5\atop p\ \mathrm{prime}}\varepsilon_m(p).
}
\tag{26}
\]

For every fixed `m`, (9) makes this sum finite and positive.

## 4. The cusp coefficient can be made arbitrarily large

Equation (6) also exposes the dependence on the chosen shift. Since `a(x)>0` decreases to zero,

\[
\varepsilon_m(p)=a(p)-a(p+m)
\uparrow a(p)
\qquad(m\to\infty)
\tag{27}
\]

for every fixed prime `p`. As `a(p)~\pi^2/(3p)` and the reciprocal-prime sum diverges, monotone convergence already implies

\[
\boxed{C_m\longrightarrow\infty}
\tag{28}
\]

along positive odd integers.

The rate is also explicit. Split the prime sum in (26) at `p=m`. From (8) and Mertens' classical theorem

\[
\sum_{p\le x}\frac1p
=\log\log x+B+o(1),
\tag{29}
\]

we obtain

\[
\sum_{p\le m}a(p)
=\frac{\pi^2}{3}\log\log m+O(1).
\tag{30}
\]

For the translated part with `p<=m`, the crude bound `a(x)=O(x^-1)` is enough:

\[
\sum_{p\le m}a(p+m)=O(1).
\tag{31}
\]

For `p>m`, (6) and `V'(t)-1=O(t^-2)` give

\[
0<\varepsilon_m(p)
\le C m p^{-2},
\]

hence, even after replacing primes by all integers,

\[
\sum_{p>m}\varepsilon_m(p)=O(1).
\tag{32}
\]

The exceptional single weight at `p=3` contributes only `O(1)`. Substituting into (26) yields

\[
\boxed{
C_m
=\frac{2\pi^2}{3}\log\log m+O(1)
\qquad(m\to\infty,\ m\ \mathrm{odd}).
}
\tag{33}
\]

Thus the coefficient of the PF-161 logarithmic cusp is not merely different for another admissible reference; it is **unbounded over a natural family of exact all-composite matched references**.

## 5. Adversarial interpretation

This result rules out the chain

```text
connected canonical bottom-Ruelle cusp coefficient
    -> intrinsic prime-flute spectral datum
    -> arithmetic/RH selector.
```

The failure is at the first arrow. `C_m` belongs to a relative selected-sector construction, and its magnitude changes with the exact all-composite reference. The family is not manufactured by an arbitrary generating function: every reference is itself an exact flute obtained from the same sampled cotangent endpoint law applied to the all-composite labels `p+m`, followed only by a Möbius translation.

Several overclaims are explicitly excluded.

- The result does **not** say that the prime flute and all `m`-shift flutes are unitarily equivalent, isospectral, or even uniformly comparable with constants independent of `m`.
- The limit `m -> infinity` is a limit through different reference surfaces; no single global metric comparison uniform in `m` is asserted.
- The logarithmic cusp remains a genuine analytic feature of each selected relative product. What fails is its interpretation as an intrinsic invariant of the prime flute.
- The divergence in (33) comes from the classical reciprocal-prime mass in the reference response, not from fluctuations of consecutive prime gaps.
- PF-158--PF-161 already warn that canonical separators form only one explicit primitive sector. Nothing here constructs or classifies a full Ruelle/Selberg object for the infinite flute.

A useful falsification test is therefore immediate: any future relative spectral or dynamical quantity proposed as a prime-flute selector must either be independent of the admissible matched reference, or specify an intrinsic rule selecting one reference and prove that the resulting datum survives replacement by the odd-shift controls above. Merely observing a distinguished boundary coefficient after one subtraction is insufficient.

## 6. Prior art and novelty audit

No novelty is claimed for the cotangent expansion, Mertens' theorem, the local Ruelle factor, or the general fact that relative determinants/zeta-type constructions depend on a comparison object. Classical relative spectral theory for noncompact hyperbolic surfaces develops reference-dependent determinants and scattering quantities under substantially different finite-geometry or hyperbolic-near-infinity hypotheses; it does not make the selected canonical separator product (20) intrinsic.

Directed searches in relative Selberg/Ruelle theory, relative determinants on infinite-area hyperbolic surfaces, and infinite-type hyperbolic geometry did not locate a theorem treating this countable canonical-separator family or the exact all-composite controls `p -> p+m`. The durable Mathia content is the project-specific exact chain

\[
\boxed{
\text{odd all-composite shift}
\to
\varepsilon_m(p)=a(p)-a(p+m)
\to
A_{a,m}
\to
C_m
\to
\frac{2\pi^2}{3}\log\log m,
}
\tag{34}
\]

combined with PF-159--PF-161 to show that the previously isolated bottom-Ruelle cusp coefficient is reference-dependent and unbounded.

The strongest novelty classification warranted is therefore **prime-flute-specific adversarial boundary/refinement**, not a new general theorem about Selberg or Ruelle zeta functions.

## Consequence for the research line

PF-161's `s log(1/s)` boundary remains mathematically correct for the `m=1` matched control, but its coefficient cannot carry an intrinsic arithmetic meaning. The full selected connected bottom-Ruelle branch is now doubly negative for RH purposes: it has no zero or pole at its boundary, and even the nonzero cusp amplitude is unstable under exact all-composite reference choice.

A surviving Ruelle/Selberg mechanism would have to come from a genuinely intrinsic full-surface object, or from a relative construction with a mathematically canonical reference whose choice itself is forced by the prime-flute geometry and survives the matched-control audit.