# PC-067 — compatible inverse-square chord energy resolves exact order but does not fix an RH scale

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `PRIOR-ART-REDIRECTION` + `DECISIVE-NEGATIVE` for using the canonical all-level inverse-square chord energy itself, or a regular scalar functional calculus of it, as the missing coercive transverse scale left open by PC-065/PC-066.

## Claim

PC-064 identifies the all-level compatible-circle completion with the arithmetic solenoid and its anchor fiber with `\widehat{\mathbb Z}`. PC-065 shows that the bare leafwise Laplacian is too soft at rational frequencies, while PC-066 shows that abstract transverse translation/unit symmetry fixes exact-order projectors but does not fix their spectral scale. A natural remaining possibility is that the **embedded Euclidean chord geometry** of the finite root sets breaks the abstract unit symmetry and canonically supplies that missing transverse scale.

For the inverse-square chord Laplacian already studied at finite level in PC-032/PC-039, let

\[
(\mathcal L_n f)(a)
=\sum_{b\ne a}
\frac{f(a)-f(b)}{|\zeta_n^a-\zeta_n^b|^2},
\qquad a\in\mathbb Z/n\mathbb Z.
\]

If `m\ge1`, let

\[
J_{n,m}:\mathbb C^{\mathbb Z/n\mathbb Z}
\longrightarrow
\mathbb C^{\mathbb Z/mn\mathbb Z},
\qquad
(J_{n,m}f)(x)=f(x\bmod n),
\]

which is the pullback induced by the intrinsic power map `z\mapsto z^m`. With normalized counting inner products these pullbacks are isometries.

Then

\[
\boxed{Q_n:=n^{-2}\mathcal L_n}
\]

satisfies the exact compatibility law

\[
\boxed{Q_{mn}J_{n,m}=J_{n,m}Q_n.}
\]

Moreover `n^{-2}` is, up to one global scalar, the **unique scalar normalization** of `\mathcal L_n` with this compatibility.

The compatible family therefore defines a bounded positive operator `Q_\perp` on

\[
L^2(\widehat{\mathbb Z})
=\overline{\bigcup_n L^2(\mathbb Z/n\mathbb Z)}.
\]

For `\gamma\in\mathbb Q/\mathbb Z`, let `r\in[0,1)` be its standard representative. Then

\[
\boxed{
Q_\perp\chi_\gamma
=\sigma(\gamma)\chi_\gamma,
\qquad
\sigma(\gamma)=\frac12r(1-r).
}
\]

This is genuinely more geometric than the unit-invariant class of PC-066: `\sigma(a/n)` is not constant on primitive residues modulo `n`, so the Euclidean embedding breaks `\widehat{\mathbb Z}^{\times}` symmetry.

The native energy nevertheless fails as the missing transverse Hamiltonian. Its spectrum lies in `[0,1/8]`, and

\[
\sigma(1/n)=\frac{n-1}{2n^2}\longrightarrow0
\]

while `\operatorname{ord}(1/n)=n\to\infty`. Thus growing conductor is soft rather than coercive; `Q_\perp` has no compact resolvent and `e^{-tQ_\perp}` is never trace class.

There is an important information-theoretic correction to a naive no-go: the multiplier does **not lose exact order**. Since

\[
r(1-r)=s(1-s)
\iff
s=r\ \text{or}\ s=1-r,
\]

and reflection preserves the denominator of a reduced rational, the eigenvalue `\sigma(\gamma)` determines `\operatorname{ord}(\gamma)`. Thus every exact-order projector from PC-066 is a Borel spectral projector of `Q_\perp`.

For `n\ge2` put

\[
S_n=
\left\{
\frac12\frac an\left(1-\frac an\right):
1\le a<n,\ (a,n)=1
\right\},
\qquad
S_1:=\{0\}.
\]

Then the `S_n` are pairwise disjoint and

\[
\boxed{
P_n=\mathbf1_{S_n}(Q_\perp),
\qquad
C=\sum_{n\ge1}nP_n=F_{\rm ord}(Q_\perp).
}
\]

Here `F_{\rm ord}` is defined by `F_{\rm ord}|_{S_n}=n`; on non-eigen spectral points it may be extended arbitrarily, since the spectral measure of `Q_\perp` on this character basis is purely atomic. This decoder is necessarily highly discontinuous.

The recovered conductor operator is exactly the classical PC-066 operator:

\[
\boxed{
\operatorname{Tr}(C^{-s})
=\sum_{n\ge1}\frac{\varphi(n)}{n^s}
=\frac{\zeta(s-1)}{\zeta(s)}.
}
\]

More generally every choice `h(n)` is equally available as the Borel function `h(C)`. Embedded chord geometry therefore restores the **information** hidden by abstract unit symmetry, but it still does not select a distinguished coercive scale, gamma factor, `s\leftrightarrow1-s` symmetry, or critical line.

## 1. Refinement compatibility fixes the scale exactly

PC-032 records the classical Fourier spectrum

\[
\mathcal L_n e_k
=\lambda_k^{(n)}e_k,
\qquad
\lambda_k^{(n)}=\frac{k(n-k)}2,
\qquad 0\le k<n,
\]

for `e_k(a)=e^{2\pi ika/n}`.

Under `J_{n,m}`, the mode `e_k` becomes the frequency-`mk` mode at level `mn`. Hence

\[
\lambda_{mk}^{(mn)}
=\frac{mk(mn-mk)}2
=m^2\lambda_k^{(n)}.
\]

Therefore

\[
\frac{\lambda_{mk}^{(mn)}}{(mn)^2}
=\frac{\lambda_k^{(n)}}{n^2},
\]

which proves

\[
Q_{mn}J_{n,m}=J_{n,m}Q_n.
\]

Now suppose `T_n=c_n\mathcal L_n` is any nonzero scalar-normalized family satisfying the same pullback law. On any nonconstant Fourier mode,

\[
c_{mn}m^2\lambda_k^{(n)}=c_n\lambda_k^{(n)},
\]

so

\[
\boxed{c_{mn}=m^{-2}c_n.}
\]

Thus `c_nn^2` is unchanged on passage to a multiple. Given arbitrary `n,r\ge2`, compare both with `\operatorname{lcm}(n,r)` to obtain

\[
c_nn^2=c_rr^2.
\]

Hence

\[
\boxed{c_n=Cn^{-2}.}
\]

The refinement geometry itself fixes the scaling exponent; `n^{-2}` is not chosen because it makes a desired spectral limit appear.

## 2. The compatible limit is an embedded transverse multiplier

The inverse system

\[
\widehat{\mathbb Z}=\varprojlim_n\mathbb Z/n\mathbb Z
\]

has normalized Haar measure, and locally constant cylinder functions are the inductive union of the finite quotient spaces under the isometries `J_{n,m}`.

For the character represented by `\gamma=k/n\pmod1`, with standard representative `r\in[0,1)`, compatibility gives

\[
\frac{\lambda_k^{(n)}}{n^2}
=\frac12r(1-r).
\]

Since

\[
0\le\frac12r(1-r)\le\frac18,
\]

the cylinder operator extends uniquely to a bounded positive self-adjoint operator satisfying

\[
\boxed{0\le Q_\perp\le\frac18 I.}
\]

It breaks the abstract unit symmetry. For example,

\[
\sigma(1/5)=\frac{2}{25},
\qquad
\sigma(2/5)=\frac{3}{25}.
\]

Thus PC-066's exact-order-only classification does not apply to this embedded operator: the circular placement retains more than order.

## 3. The native chord energy does not penalize conductor growth

PC-065 left open the possibility that an embedded transverse term might penalize the rational soft modes `1/n`. The compatible chord energy instead gives

\[
\boxed{
\sigma(1/n)=\frac{n-1}{2n^2}\sim\frac1{2n}.
}
\]

There are therefore infinitely many orthogonal nonconstant modes whose chord energy tends to zero while exact order tends to infinity.

Because `Q_\perp` is bounded on an infinite-dimensional Hilbert space, no resolvent `(Q_\perp-z)^{-1}` with `z` outside its spectrum can be compact: if it were compact and invertible, the identity would be compact. Likewise, for every `t>0`,

\[
e^{-tQ_\perp}\ge e^{-t/8}I
\]

on the character basis, so

\[
\boxed{\operatorname{Tr}(e^{-tQ_\perp})=\infty.}
\]

Every continuous functional calculus `f(Q_\perp)` is again bounded because `[0,1/8]` is compact, and therefore cannot yield compact resolvent.

A rational or meromorphic scalar transform with only finitely many singularities also cannot make the rational modes proper. Choose a compact subinterval of `(0,1/8)` avoiding those singularities. The set

\[
\{\sigma(\gamma):\gamma\in\mathbb Q/\mathbb Z\}
\]

is dense in `[0,1/8]`, so infinitely many modes remain where the transformed energy is bounded. Its resolvent is still noncompact.

Thus the missing conductor penalty is not produced by an ordinary analytic reparametrization of the native chord energy.

## 4. The exact chord eigenvalue nevertheless determines exact order

Suppose `r,s\in[0,1)` and `\sigma(r)=\sigma(s)`. Then

\[
r-r^2=s-s^2,
\]

hence

\[
(r-s)(1-r-s)=0.
\]

Therefore

\[
\boxed{s=r\quad\text{or}\quad s=1-r.}
\]

If `r=a/n` is reduced, both `a/n` and `(n-a)/n` have exact denominator `n`. Distinct exact orders therefore have disjoint eigenvalue sets `S_n`.

Consequently the spectral measure of `Q_\perp` recovers the exact-order decomposition:

\[
\boxed{P_n=\mathbf1_{S_n}(Q_\perp),\qquad \operatorname{rank}P_n=\varphi(n).}
\]

The embedded chord spectrum has not forgotten the primitive-shell partition. It encodes that partition inside a bounded dense spectral set rather than as a proper energy scale.

## 5. Discontinuous decoding returns to the classical conductor ambiguity

Define `F_{\rm ord}` on the point spectrum by

\[
F_{\rm ord}(t)=n\quad\text{for }t\in S_n.
\]

For completeness set `F_{\rm ord}(0)=1`; values at non-eigen points of the operator spectrum are irrelevant to the atomic spectral measure and may be fixed arbitrarily. Borel functional calculus gives

\[
C=F_{\rm ord}(Q_\perp)=\sum_{n\ge1}nP_n.
\]

This is exactly the conductor operator of PC-066, with compact resolvent and eigenvalue `n` of multiplicity `\varphi(n)`. Hence

\[
\operatorname{Tr}(C^{-s})
=\frac{\zeta(s-1)}{\zeta(s)}
\]

in its convergence half-plane, followed by the classical meromorphic continuation.

The decoder is not selected by regular spectral geometry. Exact-order points with arbitrarily large `n` are dense throughout the native chord spectral interval, so `F_{\rm ord}` is violently discontinuous. Once order has been decoded, every function

\[
h:\mathbb N\to\mathbb R
\]

is equally available as `h(C)`, including `C^\alpha`; as PC-066 already observes, such choices move the apparent zeta denominator to `\zeta(\alpha s)`.

Embedded chord geometry therefore fixes more than abstract profinite symmetry—it resolves order—but it does not explain why **one particular discontinuous function of order** should be the Hamiltonian. Choosing that function because its trace has desired zeta behavior is the arbitrary spectral-wrapper failure mode, not a derived RH mechanism.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the finite inverse-square matrix, Fourier diagonalization, profinite Fourier theory, or Borel functional calculus.

- F. Calogero and A. M. Perelomov, **Some Diophantine relations involving circular functions of rational angles**, *Linear Algebra and its Applications* 25 (1979), 91–94, is already anchored in `research/prime_circle/SOURCES.md` for the classical `\sin^{-2}` regular-polygon spectrum used in PC-032.
- PC-064 records the classical arithmetic-solenoid / `\widehat{\mathbb Z}` completion and its Pontryagin-dual description.
- PC-066 records the exact-order/Ramanujan projectors and the classical totient Dirichlet series `\zeta(s-1)/\zeta(s)`.
- The same inverse-square chord interaction lies in the classical long-range `1/\sin^2` neighborhood of Calogero-Sutherland/Haldane-Shastry models, reinforcing the prior-art boundary around the finite operator rather than suggesting a new finite spectral mechanism.

Targeted searches for a profinite/solenoidal inverse limit of this exact root-of-unity `\csc^2` Laplacian and for its use as an RH operator did not locate a source asserting the project-specific compatibility/decoding result above. That absence is not a novelty proof.

The durable Mathia contribution is the exact boundary obtained by combining the canonical refinement maps with the classical finite operator:

\[
\boxed{
\text{embedded inverse-square chord geometry}
\xrightarrow[\text{unique scale}]{\text{refinement compatibility}}
Q_\perp
\xrightarrow{\text{spectral measure}}
\{P_n\},
}
\]

while simultaneously proving

\[
\boxed{
Q_\perp\text{ is bounded/soft, and a compact conductor scale appears only after discontinuous order decoding.}
}
\]

## 7. Consequence for the research frontier

This closes a specific escape left by PC-065/PC-066: the canonical embedded **inverse-square chord** refinement does not itself provide the transverse coercivity needed to turn rational solenoid frequencies into a compact-resolvent RH spectrum. Refinement compatibility uniquely normalizes the finite operator into a bounded multiplier, and regular scalar functional calculus cannot repair that analytic failure.

At the same time, this result says not to discard embedded chord geometry as information-poor. Its eigenvalues already separate exact order up to reflection. The missing ingredient is therefore not a prime/conductor label but a **geometrically forced coercive law for using that label**.

This finding does **not** rule out:

- a noncommuting leaf–fiber operator formed before simultaneous diagonalization;
- an old/new or primitive-shell cross-level operator not reducible to the complete cyclic quotient `\mathbb Z/n\mathbb Z`;
- nonlinear geometry whose energy is not a scalar function of `Q_\perp`;
- a several-level determinant/Gram construction with intrinsically fixed dilation weights;
- or the global uniformization/accessory-parameter branch of PC-017.

The narrowed gate is

\[
\boxed{
\text{conductor information is already present; what remains unforced is the analytic scale that could use it.}
}
\]

## 8. Exact audit tests

The result has direct finite and limit falsifiers.

1. Verify `\lambda_k^{(n)}=k(n-k)/2` for `\mathcal L_n`.
2. Pull mode `k` from level `n` to level `mn` and verify it becomes frequency `mk` with unnormalized eigenvalue multiplied by `m^2`.
3. Verify `Q_{mn}J_{n,m}=J_{n,m}Q_n` for `Q_n=n^{-2}\mathcal L_n`.
4. Assume scalar compatibility `c_n\mathcal L_n` and derive `c_{mn}=m^{-2}c_n`; compare through least common multiples to prove `c_n=Cn^{-2}`.
5. Verify the limit multiplier `\sigma(\gamma)=\tfrac12r(1-r)` and `0\le\sigma\le1/8`.
6. Use `\gamma_n=1/n` to verify `\sigma(\gamma_n)\to0` although `\operatorname{ord}(\gamma_n)=n\to\infty`.
7. Solve `\sigma(r)=\sigma(s)` and verify the only ambiguity is reflection `s=1-r`, which preserves exact denominator.
8. Check `S_1=\{0\}` and that the finite sets `S_n`, `n\ge2`, are pairwise disjoint; verify `\mathbf1_{S_n}(Q_\perp)` has rank `\varphi(n)`.
9. Apply the order decoder and recover exactly the PC-066 conductor trace `\zeta(s-1)/\zeta(s)`.

Failure of items 2–4 invalidates the claimed canonical refinement scaling. Failure of items 7–8 invalidates the claim that the chord spectrum resolves exact order. A future RH mechanism evades the negative conclusion only by deriving a coercive/nonseparable operator law beyond regular scalar functional calculus of this compatible chord multiplier.