# PL-209 — Rank-one log-prime target transport remains spectrally programmable

**Status:** negative result / programmability obstruction  
**Evidence class:** `EXACT-DERIVED + CLASSICAL-RANK-ONE-PERTURBATION + DECISIVE-NEGATIVE` for the scoped rank-one target-relative route  
**Research line:** `prime_lattice`

## Claim

The most economical combination of the features left open by `PL-208` still does not supply arithmetic rigidity. Even if one requires, simultaneously,

- the exact source weights `log p`;
- a distinguished target vector;
- self-adjoint Hamiltonians and Herglotz/Nevanlinna target resolvents;
- rank-one, hence trace-class, prime-step resolvent differences;
- target-relative perturbation determinants; and
- exact compatibility around every prime square and along every factorization path,

all of that structure can be produced from an arbitrary scalar spectral measure.

Let `H` be any self-adjoint operator on a Hilbert space, let `psi` be a unit vector, and let

\[
P=|\psi\rangle\langle\psi|.
\]

For a finite-support exponent vector `alpha`, set

\[
\tau_\alpha
=\sum_p \alpha_p\log p
=\langle\alpha,(\log p)_p\rangle,
\qquad
H_\alpha=H+\tau_\alpha P.
\]

Then for `alpha=v(n)`,

\[
\tau_{v(n)}=\log n.
\]

Every prime step is therefore the exact rank-one perturbation

\[
H_{\alpha+e_p}=H_\alpha+(\log p)P.
\]

Writing

\[
R_\alpha(z)=(H_\alpha-z)^{-1},
\qquad
m_\alpha(z)=\langle\psi,R_\alpha(z)\psi\rangle,
\]

the rank-one resolvent formula gives

\[
\boxed{
 m_\alpha(z)
 =\frac{m_0(z)}{1+\tau_\alpha m_0(z)}
}
\]

and hence the exact prime transport law

\[
\boxed{
 m_{\alpha+e_p}(z)
 =\frac{m_\alpha(z)}{1+(\log p)m_\alpha(z)}.
}
\]

The corresponding prime-edge perturbation determinant is

\[
\boxed{
 \Delta_{\alpha,p}(z)
 =\det\!\bigl(I+(\log p)P R_\alpha(z)\bigr)
 =1+(\log p)m_\alpha(z).
}
\]

These determinants telescope around the lattice. Along any path from `0` to `v(n)`,

\[
\prod_{\text{edges}}\Delta_{\alpha,p}(z)
=1+(\log n)m_0(z),
\]

independently of the order in which the prime directions are traversed.

Nevertheless the target spectral data are completely programmable. For any probability measure `mu` on `R`, take

\[
\mathcal H=L^2(\mu),
\qquad
(Hf)(x)=x f(x),
\qquad
\psi(x)=1.
\]

Then

\[
\boxed{
 m_0(z)=\int_\mathbb R\frac{d\mu(x)}{x-z}.
}
\]

Thus arbitrary positive scalar spectral measures can coexist with the full package above. The prime family has used the exact arithmetic numbers `log p`, but only by inserting them as coefficients in a one-dimensional rank-one perturbation parameter. It has not forced any Riemann-specific spectral measure, continuation, determinant, or zero divisor.

Consequently the route

\[
\text{distinguished target}
+\log p\text{ rank-one steps}
+S_1\text{ resolvent data}
+\text{Herglotz positivity}
+\text{flat determinants}
\Longrightarrow
\text{RH spectral rigidity}
\]

is blocked unless an additional theorem makes the source, target, or coupling arithmetically nonprogrammable.

## Exact rank-one derivation

For a real scalar `t`, put

\[
H_t=H+tP,
\qquad
R_t(z)=(H_t-z)^{-1},
\qquad
m_t(z)=\langle\psi,R_t(z)\psi\rangle.
\]

The second resolvent identity for the rank-one perturbation gives

\[
R_t(z)
=R_0(z)
-\frac{t}{1+t m_0(z)}
 R_0(z)P R_0(z).
\]

Taking the `psi` matrix element yields

\[
m_t(z)
=m_0(z)-\frac{t m_0(z)^2}{1+t m_0(z)}
=\frac{m_0(z)}{1+t m_0(z)}.
\]

There is no pole in this formula for nonreal `z`: `H_t` is self-adjoint, so `z` belongs to its resolvent set and `1+t m_0(z)` cannot vanish there.

Now set `t=tau_alpha` and `c=log p`. Applying the same identity from `H_alpha` to `H_alpha+cP` gives

\[
R_{\alpha+e_p}(z)-R_\alpha(z)
=-(\log p)R_{\alpha+e_p}(z)P R_\alpha(z).
\]

The right-hand side has rank at most one. Hence every adjacent relative resolvent difference is finite rank and belongs to `S_1` without any spectral-density argument.

The scalar target law follows either from the preceding formula or by composition of the Möbius maps

\[
T_c(m)=\frac{m}{1+cm}.
\]

They satisfy

\[
T_c\circ T_d=T_{c+d}.
\]

Therefore the whole exponent lattice factors through the additive energy

\[
\alpha\longmapsto \tau_\alpha
=\langle\alpha,\log p\rangle,
\]

and then through a one-parameter action on the scalar target resolvent. The apparent many-prime compatibility is the associativity of scalar addition.

## Exact determinant flatness

Because `P R_alpha(z)` has rank one,

\[
\det\!\bigl(I+cP R_\alpha(z)\bigr)
=1+c\,\operatorname{Tr}(P R_\alpha(z))
=1+c m_\alpha(z).
\]

Using

\[
m_\alpha(z)=\frac{m_0(z)}{1+\tau_\alpha m_0(z)},
\]

we obtain

\[
1+c m_\alpha(z)
=\frac{1+(\tau_\alpha+c)m_0(z)}{1+\tau_\alpha m_0(z)}.
\]

Thus two successive prime steps satisfy

\[
\Delta_{\alpha,p}(z)
\Delta_{\alpha+e_p,q}(z)
=
\frac{1+(\tau_\alpha+\log p+\log q)m_0(z)}
     {1+\tau_\alpha m_0(z)},
\]

which is unchanged when `p` and `q` are exchanged. More generally every path telescopes, and at `alpha=v(n)` the endpoint ratio is

\[
\frac{1+(\tau_0+\log n)m_0(z)}{1+\tau_0m_0(z)}
=1+(\log n)m_0(z).
\]

Hence even a target-relative determinant law that explicitly knows `log p`, closes every prime square, and recovers `log n` at the endpoint can be a tautological one-dimensional perturbation cocycle.

This strengthens the programmability warning in `PL-208`. There the operator-valued transfer was generic for arbitrary bounded prime perturbations. Here the perturbation family is much more special—rank one, fixed target, exact `log p` coefficient, positive scalar Weyl function—and the same absence of arithmetic rigidity remains.

## Herglotz positivity is also automatic

For `z=x+iy` with `y>0`, the spectral theorem gives

\[
m_0(z)
=\int_\mathbb R\frac{d\mu_\psi(\lambda)}{\lambda-z},
\]

so

\[
\operatorname{Im}m_0(z)
=\int_\mathbb R
\frac{y}{(\lambda-x)^2+y^2}
\,d\mu_\psi(\lambda)
>0
\]

for nonzero `psi`. Thus the scalar target resolvent is a Herglotz/Nevanlinna function for every self-adjoint source. Positivity has not selected the arithmetic model; it is a universal consequence of self-adjointness.

The matched control is particularly strong because the converse realization needed here is elementary. Given any probability measure `mu`, multiplication by `x` on `L^2(mu)` is self-adjoint on its natural domain and the unit vector `psi=1` has scalar spectral measure exactly `mu`. The formula

\[
m_0(z)=\int (x-z)^{-1}d\mu(x)
\]

then produces all the prime-step identities above.

One may therefore prescribe, for example, arbitrary finite atomic target spectra and weights before the prime lattice is attached. The later appearance of exact `log p` increments, trace-class relative resolvents, positive target resolvents, and flat Fredholm determinants does not retroactively make that spectrum arithmetic.

## Relation to the accepted trace-class clue

`PL-034` already showed that trace-class regularity and perturbation determinants are too flexible in ordinary shift/extension models, while the canonical Bost–Connes residual cocycle is zero. `PL-208` showed that even spectral-parameter-dependent, invertible, holomorphic, flat operator transport is generic for bounded perturbation lattices.

The present control addresses a narrower combination that survived those findings. It includes a distinguished target vector and the exact prime energy weights rather than arbitrary `V_p`. Those extra ingredients still do not help when they enter through the single fixed rank-one projection `P`:

\[
H_\alpha=H+\langle\alpha,\log p\rangle P.
\]

The accepted clue therefore remains open only beyond this scalarized target architecture. A useful relative invariant must obtain its `log p` dependence and target coupling from the arithmetic construction itself and must carry information that cannot be reproduced by choosing an arbitrary scalar spectral measure first.

## Analytic-continuation boundary

No Euler product and no analytic continuation of zeta are used in this countermodel. That is precisely its role: it shows that the listed operator properties can all hold in systems having no zeta function at all.

Accordingly, none of those properties by itself can constitute the missing bridge from the absolutely convergent Euler-product region to the critical strip. A viable zeta construction must add an independent identity tying the operator data to the analytically continued completed zeta function, the Nyman target, the explicit formula, Weil positivity, or another nonprogrammable arithmetic observable.

## Prior art and novelty audit

The rank-one resolvent identity, scalar Weyl/Herglotz function, rank-one Fredholm determinant, and spectral-measure realization are classical operator theory. `PL-034` already anchors the line's use of classical trace-class perturbation determinants, and all identities needed for the present obstruction have been re-derived explicitly above.

A targeted novelty audit around Aronszajn–Krein rank-one perturbations, Weyl/Herglotz functions, perturbation determinants, and logarithmic prime weights found the ambient rank-one machinery to be classical. No novelty is claimed for any operator-theoretic ingredient, and absence of an exact phrase in the literature is not used as evidence. The durable delta is only the line-specific matched control: inserting the canonical weights `log p` and a distinguished target into this rank-one architecture still leaves the target spectral measure arbitrary.

## Adversarial boundaries

**The result is scoped to a fixed rank-one target coupling.** It does not classify higher-rank, noncommuting, singular, domain-changing, adelic, or genuinely target-relative prime actions in which different primes act through distinct operator directions.

**Using the true numbers `log p` is not the same as deriving them.** The countermodel deliberately uses the exact rational-prime weights. Its point is that source-label fidelity alone is insufficient: one can paste those weights onto arbitrary spectral data. A successful construction must prove that the arithmetic source forces the coupling rather than select it by hand.

**The scalar determinant may still be useful when canonically identified with an arithmetic function.** This finding does not say a determinant of the form `1+t m(z)` can never carry arithmetic information. It says its positivity, trace-class origin, and lattice chain law do not supply that information. An independent theorem identifying `m` or the determinant with a zeta-specific object would be extra content and must be audited on its own.

**Self-adjointness does not prove RH merely because the control spectrum is real.** The arbitrary-measure realization shows why. A self-adjoint operator with freely chosen spectral measure is easy to manufacture; the hard Hilbert–Pólya step is a canonical theorem identifying its spectrum with the Riemann zero ordinates without already assuming their localization.

**The prime lattice is compressed to one dimension.** All prime paths enter only through `tau_alpha=<alpha,log p>`. A construction with irreducible multi-prime curvature, noncommuting local data, or a global trace law that cannot factor through `log n` lies outside the obstruction.

## Falsification / audit tests

The exact construction would fail if any of the following were false:

1. the rank-one resolvent formula gives `m_t=m_0/(1+t m_0)` for `H_t=H+tP`;
2. adjacent resolvent differences have rank at most one;
3. the rank-one perturbation determinant equals `1+c m_t`;
4. the determinant factors telescope under successive additive perturbations;
5. every probability measure on `R` can occur as the scalar spectral measure of `psi=1` for a multiplication operator.

These are standard/direct calculations. The research conclusion would be materially narrowed by a theorem showing that the specific zeta/prime-lattice source enforces an additional relation on `m`, `P`, or the joint prime family that cannot be reproduced in the arbitrary-measure model.

## Consequence for the research line

The operator frontier after `PL-208` is narrower than merely demanding exact `log p` normalization, a distinguished target, positivity, or a trace-class determinant. Even their rank-one combination is programmable and collapses through

\[
v(n)
\longmapsto \log n
\longmapsto
\frac{m_0}{1+(\log n)m_0}.
\]

A surviving mechanism must therefore contain genuinely nonprogrammable arithmetic data. Plausible escape classes include a source-forced target/coupling derived from the Nyman or explicit-formula structures, an irreducibly multi-prime operator law that does not factor through `log n`, or a global positivity/trace identity whose failure can be demonstrated on the arbitrary-measure matched controls above. Merely adding `log p` labels to standard rank-one perturbation theory does not cross that gate.
