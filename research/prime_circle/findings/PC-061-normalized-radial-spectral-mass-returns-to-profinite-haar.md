# PC-061 — normalized radial spectral mass returns weakly to profinite Haar

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the most canonical scalar renormalization left open by PC-060. Let

\[
L(x):=-\log(1-x),\qquad 0<x<1,
\]

and normalize the escaped PC-060 spectral measure to unit mass,

\[
\boxed{
\bar\nu_x
:=\frac1{L(x)}\sum_{n\ge1}\frac{x^n}{n}\,\delta_n,
}
\]

where the positive integers are embedded diagonally in the profinite integers `\widehat{\mathbb Z}`. Then

\[
\boxed{
\bar\nu_x\Longrightarrow m_{\widehat{\mathbb Z}}
\qquad(x\to1^-),
}
\]

weakly, where `m_{\widehat{\mathbb Z}}` is normalized Haar measure. Equivalently, every nontrivial finite-conductor additive Fourier mode tends to zero. Under the valuation quotient this limit is exactly the PC-059 product law

\[
\mu=\bigotimes_p\mu_p,
\qquad
\mu_p(j)=\left(1-\frac1p\right)p^{-j}.
\]

Thus the natural probability normalization of the singular atomic mass from PC-060 does not produce a new finite-adic spectral measure at the boundary. It returns to the same classical profinite Haar vacuum measure already identified in PC-059.

## 1. The canonical probability normalization of the PC-060 mass

PC-060 proves that the eigenvalue-weighted projective-limit measure for the exact radial kernel

\[
F_x(n)=-\log(1-x^n)
\]

is

\[
\nu_x=\sum_{n\ge1}\frac{x^n}{n}\delta_n,
\qquad
\nu_x(\widehat{\mathbb Z})=L(x).
\]

For each fixed `x<1` this measure is concentrated on the embedded positive integers, a countable Haar-null subset of `\widehat{\mathbb Z}`. PC-060 therefore leaves open a natural boundary question: after dividing by the only scalar that makes the measure a probability, can the limit `x\to1^-` carry a nontrivial finite-adic spectral distribution?

The normalized measure is the classical logarithmic-series law viewed inside the profinite completion:

\[
\bar\nu_x(\{n\})=rac{x^n}{nL(x)}.
\]

The answer to the boundary question is exact and negative.

## 2. Every nontrivial profinite additive Fourier mode vanishes

Every continuous additive character of `\widehat{\mathbb Z}` has finite conductor. Write one as

\[
\chi_{a,q}(n)=e^{2\pi i an/q},
\qquad a\in\mathbb Z/q\mathbb Z.
\]

Let `\zeta_q=e^{2\pi i/q}`. Directly from the logarithmic power series,

\[
\begin{aligned}
\widehat{\bar\nu_x}(a,q)
&=\int\chi_{a,q}(y)\,d\bar\nu_x(y)\\
&=\frac1{L(x)}\sum_{n\ge1}\frac{(x\zeta_q^a)^n}{n}\\
&=\boxed{
\frac{-\Log(1-x\zeta_q^a)}{-\log(1-x)}
}.
\end{aligned}
\]

Here `Log` denotes the analytic branch selected by the convergent power series for `|x|<1`. If `a\equiv0\pmod q`, the ratio is identically `1`. If the character is nontrivial, `\zeta_q^a\ne1` and Abel convergence gives

\[
-\Log(1-x\zeta_q^a)\longrightarrow-\Log(1-\zeta_q^a),
\]

a finite value, while `L(x)\to\infty`. Hence

\[
\boxed{
\widehat{\bar\nu_x}(\chi)\longrightarrow
\begin{cases}
1,&\chi=1,\\
0,&\chi\ne1.
\end{cases}}
\]

For every fixed nontrivial conductor the decay is in fact

\[
\widehat{\bar\nu_x}(\chi)=O_\chi\!\left(\frac1{L(x)}\right).
\]

This is exactly the Fourier transform of normalized Haar measure on the compact abelian group `\widehat{\mathbb Z}`.

## 3. Weak convergence to Haar is therefore forced

Finite-conductor characters form the Pontryagin dual of `\widehat{\mathbb Z}` and their finite linear combinations are uniformly dense in the continuous functions on the compact group. The preceding Fourier limits therefore imply

\[
\boxed{
\bar\nu_x\Longrightarrow m_{\widehat{\mathbb Z}}
\qquad(x\to1^-).
}
\]

The same statement is visible without Fourier language. For every residue class `b mod q`, the root-of-unity filter gives

\[
\sum_{\substack{n\ge1\\n\equiv b\ (q)}}\frac{x^n}{n}
=\frac1q\sum_{r=0}^{q-1}
\zeta_q^{-br}\bigl[-\Log(1-x\zeta_q^r)\bigr].
\]

Only the `r=0` term diverges as `x\to1^-`; all others stay bounded. Therefore

\[
\boxed{
\bar\nu_x\{n\equiv b\pmod q\}
=\frac1q+O_q\!\left(\frac1{L(x)}\right)
\longrightarrow\frac1q.
}
\]

So the escaping logarithmic-series atoms become asymptotically uniform in every fixed finite quotient `\mathbb Z/q\mathbb Z`, which is precisely the projective definition of Haar measure on `\widehat{\mathbb Z}`.

## 4. The valuation quotient reproduces PC-059 exactly

The compatibility with PC-059 can be checked directly. Fix a finite set of primes `S` and exponents `a_p\ge0`, and put

\[
q=\prod_{p\in S}p^{a_p}.
\]

The cylinder condition `v_p(n)\ge a_p` for every `p\in S` is just divisibility by `q`. Hence

\[
\begin{aligned}
\bar\nu_x(q\mid n)
&=\frac1{L(x)}\sum_{k\ge1}\frac{x^{qk}}{qk}\\
&=\boxed{
\frac1q\frac{L(x^q)}{L(x)}
}
\longrightarrow\frac1q,
\end{aligned}
\]

because

\[
L(x^q)=L(x)-\log q+o(1).
\]

Taking finite differences in the exponents yields, for any prescribed finite valuation pattern,

\[
\boxed{
\bar\nu_x\{v_p(n)=j_p\text{ for }p\in S\}
\longrightarrow
\prod_{p\in S}\left(1-\frac1p\right)p^{-j_p}.
}
\]

Those are exactly the local factors of the PC-059 valuation pushforward of profinite Haar measure. Thus PC-060's singular atomic energy measure and PC-059's nonatomic vacuum law are not two competing boundary spectra: after the natural total-mass normalization and boundary limit, the former converges weakly back to the latter.

## 5. The convergence is weak only: the integer sector remains singular at every finite `x`

There is an important boundary condition. For every `0<x<1`,

\[
\bar\nu_x(\mathbb N)=1,
\qquad
m_{\widehat{\mathbb Z}}(\mathbb N)=0.
\]

Therefore

\[
\boxed{
\bar\nu_x\perp m_{\widehat{\mathbb Z}}
\quad\text{for every }x<1.
}
\]

The probability total-variation distance stays maximal even though weak convergence holds. The disappearing distinction is therefore exactly the distinction visible to **continuous profinite-local observables**. A discontinuous observable that singles out the embedded countable integer sector can retain it, but such an observable is not supplied by the compact profinite topology itself.

This prevents overreading the theorem: the boundary limit does not say that the atomic and Haar measures become close in a strong norm. It says that every fixed finite quotient and every fixed continuous additive mode forgets the atomic support in the limit.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the ambient mechanism.

- The embedding `\mathbb Z\hookrightarrow\widehat{\mathbb Z}`, normalized Haar measure on the profinite completion, and characterization of Haar by vanishing nontrivial continuous characters are standard compact-abelian/Pontryagin theory.
- Uniform distribution in all fixed residue quotients is the standard projective signature of Haar measure on `\widehat{\mathbb Z}`.
- The weights `x^n/n` and their normalization are the classical logarithmic-series distribution already identified in PC-060; the displayed character transform is the elementary logarithmic generating function.
- A close modern arithmetic-density boundary is Luca Demangos and Ignazio Longhi, **Densities on Dedekind domains, completions and Haar measure**, *Mathematische Zeitschrift* 306:2 (2024), DOI `10.1007/s00209-023-03415-2`, arXiv:2009.04229. They systematically study when arithmetic densities on `S`-integers agree with Haar measure on profinite completions. The present Abel/logarithmic weighting is a specialized elementary instance rather than evidence for a new profinite density theory.

The project-specific exact consequence is narrower: combining the specific PC-060 spectral atoms with the PC-059 profinite spectral representation shows that the most canonical scalar boundary normalization closes a previously explicit escape route by returning to the already classified Haar vacuum.

## 7. Why this is a decisive negative for the normalized finite-adic boundary route

PC-060 closed the **unrenormalized** infinite-symbol route but explicitly left geometrically justified renormalization open. The first and most canonical scalar renormalization is forced once one asks for a probability spectral measure: divide by the total mass `L(x)`. PC-061 shows that this does not expose a hidden finite-adic critical-line object. It produces

\[
\boxed{
\text{PC-060 atomic escaped mass}
\xrightarrow{\,/L(x)\,}
\text{log-series probability}
\xrightarrow{x\to1^-}
\text{PC-059 profinite Haar vacuum}.
}
\]

All fixed finite-conductor Fourier data except the trivial mode vanish. There is no free complex spectral parameter, no gamma factor, no intrinsic `s\leftrightarrow1-s` symmetry and no selector for `\Re(s)=1/2`. The only divergence is the elementary logarithmic normalization `L(x)`.

Therefore the route

\[
\boxed{
\text{exact radial prime-circle energy}
\to
\text{escaped arithmetic atoms}
\to
\text{normalize total mass}
\to
\text{new profinite boundary spectrum}
\to
\text{RH}
}
\]

is closed.

What remains outside the obstruction is more specific: a conductor growing together with the boundary scale; a noncontinuous/global observable that intrinsically retains the embedded integer sector; a non-scalar renormalization independently forced by two-dimensional geometry; an archimedean/finite-adic self-duality derived rather than appended; nonlinear or nonseparable cross-level coupling; or the global primitive-root uniformization/accessory branch of PC-017. None of those is supplied by the present radial divisor-Haar family, and introducing a growing conductor or new renormalization merely by choice would be an external scale wrapper unless the original geometry forces it.

## 8. Exact audit tests

The claim can be falsified without asymptotic numerics:

1. for any `q,a`, check directly that the additive-character transform is `-Log(1-x zeta_q^a)/L(x)`;
2. for `a\not\equiv0 mod q`, verify that the numerator has a finite Abel limit while `L(x)` diverges;
3. use the finite root-of-unity filter to recover probability `1/q+O_q(1/L(x))` for every residue class;
4. verify the divisibility-cylinder identity `bar nu_x(q|n)=q^{-1}L(x^q)/L(x)` and recover the PC-059 valuation probabilities by finite differences;
5. verify separately that every `bar nu_x` is supported on the Haar-null embedded integers, so the convergence cannot be strengthened to total variation.

Failure of any one of the first four exact identities would invalidate the Haar-limit conclusion. A different renormalization evades the result only by supplying additional structure not present in the canonical total-mass normalization.