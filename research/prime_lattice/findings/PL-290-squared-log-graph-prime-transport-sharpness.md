# PL-290 — Squared-log graph regularity is sharp for source-static prime transport

**Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE/ROUTE-RESTRICTION + PRIME-LATTICE/KRONECKER`

**Status:** `GRAPH-NORM-SHARPNESS + NO-UNIFORM-C1-APERTURE-DERIVATIVE`

## Claim

`PL-289` upgrades actual localized-Weil eigenstates from the logarithmic form domain to the operator graph domain and hence gives a squared-log Fourier moment. That gain is real, but it is also the exact generic endpoint of the graph-domain information.

On the source-static aperture interval

\[
J=\left(\frac{\log 4}{2},\frac{\log 5}{2}\right),
\]

the active prime powers in Suzuki's fixed-domain localized Weil form are `2,3,4`. Let

\[
h_n(a)=\frac{\log n}{a},\qquad c_n=\frac{\Lambda(n)}{\sqrt n},
\]

and for zero extension outside `I=(-1,1)` write

\[
q_h(w)=\langle S_h w,w\rangle
=\int_{-1}^{1-h}w(x+h)\overline{w(x)}\,dx,
\qquad 0<h<2.
\]

The moving arithmetic part is

\[
P_a(w)=-2\sum_{n\in\{2,3,4\}}c_n\,\Re q_{h_n(a)}(w).
\]

Let `T` be the principal logarithmic operator of `PL-289`, with

\[
m(\xi)=\log|\xi|+\gamma,
\]

and use its graph-equivalent quadratic norm

\[
\mathcal G_2(w)
:=\|w\|_2^2+
\frac1{2\pi}\int_{\mathbb R}m(\xi)^2|\widehat{Ew}(\xi)|^2\,d\xi,
\qquad w\in D(T).
\]

Then, for every fixed `a in J`,

\[
\boxed{
\sup_{0\ne w\in D(T)}
\frac{|P_b(w)-P_a(w)|}{\mathcal G_2(w)}
=
\Theta\!\left(\frac1{\log^2(1/|a-b|)}\right)
\qquad (b\to a).
}
\]

More explicitly, putting

\[
A_n(a)=2-\frac{\log n}{a},
\]

one has

\[
\boxed{
\liminf_{b\to a}
\log^2\frac1{|a-b|}
\sup_{0\ne w\in D(T)}
\frac{|P_b(w)-P_a(w)|}{\mathcal G_2(w)}
\ge
2\bigl(c_2A_2(a)+c_3A_3(a)\bigr)>0.
}
\]

At `a=0.8`, this lower constant is approximately

\[
1.9062429603.
\]

The scalar and continuous-kernel terms of Suzuki's source-static fixed-domain form are locally Lipschitz in `a` relative to `L^2`, while the principal logarithmic form is independent of `a`. Hence the **complete source-static fixed-domain Weil form has the same sharp inverse-squared-log graph-norm modulus**.

Consequently, the graph-domain theorem of `PL-289` cannot by itself produce a locally Lipschitz, let alone uniformly differentiable, aperture family in the natural graph-form topology. In particular, there is no automatic graph-norm Feynman--Hellmann route that turns the aperture motion into a bounded first derivative. Any stronger transport estimate must use information special to the actual low eigenbranch, an arithmetic cancellation identity, or a stronger state-specific norm than membership in `D(T)`.

## 1. Upper bound from the squared-log moment

`PL-289` proves that for every normalized `w` with finite squared-log energy,

\[
|q_{h+\delta}(w)-q_h(w)|
\le E_2(w)\,\omega_2(\delta),
\]

where

\[
E_2(w)=\frac1{2\pi}\int
\bigl(1+(\log^+|\xi|)^2\bigr)|\widehat{Ew}(\xi)|^2\,d\xi
\]

and

\[
\omega_2(\delta)=\frac{2+o(1)}{\log^2(1/|\delta|)}.
\]

The weights `1+(log^+|xi|)^2` and `1+m(xi)^2` are equivalent, so `E_2` and `mathcal G_2` are equivalent norms on `D(T)`.

For fixed `a in J` and `b->a`,

\[
\delta_n(a,b)=h_n(b)-h_n(a)
=(\log n)\left(\frac1b-\frac1a\right),
\]

hence

\[
\log\frac1{|\delta_n(a,b)|}
=
\log\frac1{|a-b|}+O(1)
\]

for each of the three active channels. Summing the three estimates with the fixed coefficients `c_n` gives

\[
\sup_{0\ne w\in D(T)}
\frac{|P_b(w)-P_a(w)|}{\mathcal G_2(w)}
=
O\!\left(\frac1{\log^2(1/|a-b|)}\right).
\]

Thus the only remaining question is sharpness: could the zeta-specific combination `2,3,4` cancel the leading graph-domain transport just as the individual channels move together? It cannot.

## 2. Modulated interval states lie in the exact graph domain

Take

\[
w_\xi(x)=e^{i\xi x},\qquad x\in(-1,1),
\]

with zero extension to `R`. Its Fourier transform is a translate of the Fourier transform of `1_I`, and

\[
|\widehat{1_I}(\eta)|=O(|\eta|^{-1}).
\]

Therefore

\[
\int_{\mathbb R}(1+\log^2(2+|\eta|))
|\widehat{1_I}(\eta)|^2\,d\eta<\infty.
\]

By the exact characterization in `PL-289`, every `w_xi` belongs to `D(T)`. Translation of the Fourier profile then gives

\[
\boxed{
\mathcal G_2(w_\xi)
=(2+o(1))\log^2|\xi|
\qquad(|\xi|\to\infty).
}
\]

The coefficient `2` is `||1_I||_2^2`. The logarithmic singularity near frequency zero causes no issue: after modulation it occupies a region carrying only the `O(|eta|^{-2})` tail of the translated sinc profile, while the bulk of the Fourier mass sees `log|xi|+O(1)`.

The autocorrelation is exact:

\[
q_h(w_\xi)=(2-h)e^{i\xi h}.
\]

Thus these graph-domain states retain the same phase-control mechanism used in `PL-286`, but their cost is now quadratic rather than linear in `log|xi|`.

## 3. Prime-lattice phase locking proves sharpness

Put

\[
d=\frac1b-\frac1a.
\]

The phase increment of the `n`-th arithmetic channel is

\[
\xi\bigl(h_n(b)-h_n(a)\bigr)=\xi d\log n.
\]

Unique factorization gives `log 2 / log 3 notin Q`, so the Kronecker flow

\[
y\longmapsto(y\log2,y\log3)\pmod{2\pi}
\]

is dense in the two-torus. As in `PL-286`, for every fixed phase tolerance `epsilon>0` choose `y=y_epsilon` so that

\[
y\log2=\pi+O(\epsilon),\qquad
y\log3=\pi+O(\epsilon)
\pmod{2\pi}.
\]

For small nonzero `d`, take

\[
\xi_d=\frac{y}{d}+t_d,
\]

where `t_d` remains bounded and is chosen, by minimality of the same irrational torus flow, so that the old `2`- and `3`-phases at aperture `a` are both `O(epsilon)` modulo `2pi`. Then

\[
|\xi_d|=\frac{|y|}{|d|}+O_\epsilon(1),
\qquad
\log|\xi_d|=\log\frac1{|d|}+O_\epsilon(1).
\]

The `2` and `3` cosines therefore move coherently from near `+1` to near `-1`. The `4` channel cannot spoil the witness because

\[
\log4=2\log2:
\]

its old phase is near `0` and its increment is near `2pi`, so its cosine stays near `+1`.

Consequently,

\[
P_b(w_{\xi_d})-P_a(w_{\xi_d})
=
4\bigl(c_2A_2(a)+c_3A_3(a)\bigr)
+O(\epsilon)+o_{d\to0}(1).
\]

Together with

\[
\mathcal G_2(w_{\xi_d})
=(2+o(1))\log^2\frac1{|d|}
\]

and `log(1/|d|)=log(1/|a-b|)+O(1)`, this yields

\[
\liminf_{b\to a}
\log^2\frac1{|a-b|}
\sup_{0\ne w\in D(T)}
\frac{|P_b(w)-P_a(w)|}{\mathcal G_2(w)}
\ge
2\bigl(c_2A_2(a)+c_3A_3(a)\bigr).
\]

This is strictly positive throughout `J` because `h_2(a),h_3(a)<2` there.

## 4. The full source-static form inherits the same obstruction

Suzuki's fixed-domain decomposition on `J` has four pieces:

1. the `a`-independent principal logarithmic form;
2. a scalar term containing `-log a`;
3. the finite prime-power translation comb `P_a`;
4. a continuous-kernel remainder depending smoothly on `a`.

On a compact subinterval of `J`, the scalar and continuous-kernel differences are

\[
O(|a-b|)\,\|w\|_2^2.
\]

For the phase-locked witnesses `w_{xi_d}`, this contribution is `O(|a-b|)`, whereas the prime-comb difference tends to the nonzero constant displayed above. Hence these smoother terms cannot cancel the lower bound. The upper bound follows by combining their Lipschitz estimate with the squared-log estimate for `P_a`.

Therefore the complete source-static form has graph-norm transport modulus `Theta(log^-2)`.

## 5. No uniform graph-norm aperture derivative

Let

\[
\|Q_b-Q_a\|_{\mathcal G_2}
:=
\sup_{0\ne w\in D(T)}
\frac{|Q_b(w)-Q_a(w)|}{\mathcal G_2(w)}
\]

for the fixed-domain quadratic forms. The previous sections show

\[
\|Q_b-Q_a\|_{\mathcal G_2}
\asymp
\frac1{\log^2(1/|a-b|)}.
\]

Hence

\[
\frac{\|Q_b-Q_a\|_{\mathcal G_2}}{|a-b|}
\longrightarrow\infty.
\]

So the common graph domain supplied by `PL-289` does **not** make the aperture family locally Lipschitz or differentiable in this natural bounded-form norm. This does not assert that an individual isolated eigenvalue branch cannot possess a derivative, nor that a smoother individual eigenstate cannot satisfy a Feynman--Hellmann identity. It says that neither conclusion follows uniformly from the currently proved graph-domain regularity.

That distinction matters for the live positivity-transport problem. A formal differentiation of the moving prime shifts would introduce the generator of translation, i.e. a factor `xi` in Fourier space. Squared-log control is far weaker than an `xi^2` moment and does not justify that operation. Any derivative/cancellation identity for the ground branch must therefore be proved from additional structure rather than inferred from `D(T)`.

## 6. Adversarial audit

**Witness admissibility.** The modulated indicators have endpoint jumps, but the exact graph-domain theorem of `PL-289` admits them because their Fourier tails are `O(|xi|^-1)` and squared logarithms remain integrable. No hidden `H^1` assumption is used.

**Prime-comb cancellation.** The lower bound locks the independent prime directions `2` and `3` while the dependent `4=2^2` direction executes a full phase turn. Thus the lower bound is for the full active zeta comb, not a single source channel.

**Remainder cancellation.** The non-arithmetic source-static terms change by `O(|a-b|)` on the `L^2`-normalized witness, so they are asymptotically too small to cancel an `O(1)` prime-comb numerator.

**Norm choice.** `mathcal G_2` is graph-equivalent, not a new arithmetic norm. Replacing it by `||w||_2^2+||Tw||_2^2` changes constants but not the inverse-squared-log sharp order by `PL-289`.

**Eigenstates versus graph ball.** The witness is not claimed to be a ground state. This result deliberately closes only the generic graph-domain escape. The actual eigenbranch can still enjoy additional cancellation unavailable on the full graph ball; that is now the only relevant place to seek a stronger modulus.

**Source thresholds.** The theorem is source-static. At `2a=log n`, a new prime-power channel activates and the existing threshold bookkeeping remains necessary.

## 7. Prior-art and novelty audit

The logarithmic Laplacian, its bounded-domain energy space, and translation/modulus-of-smoothness theory are established subjects. Suzuki supplies the fixed-domain Weil decomposition; `PL-286` supplies the exact zeta-comb Kronecker witness at form-domain scale; `PL-289` supplies the one-dimensional graph-domain characterization and squared-log moment.

A structure-based literature search for logarithmic-Laplacian graph norms, logarithmic smoothness spaces, translation moduli, and bounded-domain spectral theory did not reveal this specific sharp `log^-2` source-static Weil transport statement or the resulting failure of a uniform graph-norm aperture derivative. The result is therefore recorded as an **exact line-local consequence of the existing ingredients**, not as a broad novelty claim about translation semigroups or logarithmic smoothness spaces.

The underlying principle is standard: a Fourier weight growing like `log^2|xi|` permits translations to be uniformly continuous only at inverse-squared-log scale. The arithmetic content of this finding is the matched `2,3,4` phase-locking witness showing that the actual active von-Mangoldt comb saturates that generic scale.

## 8. Consequence for the research line

`PL-289` correctly removes the inverse-log form-domain barrier for actual eigenstates, but **graph-domain membership alone is now exhausted as a transport mechanism**:

\[
D(T)
\Longrightarrow
\text{squared-log moment}
\Longrightarrow
O(\log^{-2})
\]

is sharp even for the complete active zeta source comb.

The next useful theorem cannot be another generic regularity upgrade extracted solely from the already known graph domain. It must use the eigen-equation in a way that excludes the phase-locked graph witnesses: a state-specific cancellation identity, stronger regularity proved specifically for the low eigenbranch, a substantially smaller explicit moment constant, or a direct finite positivity certificate over an aperture interval. In particular, differentiating the aperture dependence is not legitimate merely from the `PL-289` squared-log moment.