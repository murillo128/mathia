# PF-266 — diagonal capacity recovers the uniform mass-mode Green amplitude

**Status:** `EXACT-DERIVED + UNIFORM-DIAGONAL-GREEN-AMPLITUDE + TWO-SIDED-CAPACITY + FINITE-SEAM-ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-264-fixed-mass-green-kernel-has-universal-two-index-leading-law|PF-264]] identifies the sharp fixed-mass Green amplitude

\[
G_{ij}^{(\varepsilon)}(a)
\sim \frac{1}{2\mu\sqrt{ij}}
\left(\frac{i}{j}\right)^\mu,
\qquad
\mu=\sqrt{1+a^2},
\]

while [[research/prime_flute/findings/PF-265-unbounded-gap-combes-thomas-makes-mass-mode-green-decay-uniform|PF-265]] makes the off-diagonal **decay metric** uniform in both mass and mode but leaves only the coarse prefactor `O(\mu^{-2})`. PF-265 therefore isolates a natural diagonal discriminator:

\[
G_{ii}^{(\varepsilon)}(a)
\lesssim \frac{1}{\mu(i+\mu)}.
\]

That discriminator is true, and in fact it is sharp up to fixed constants uniformly over the entire coupled mass/mode plane. There are constants `0<c<C<\infty`, independent of parity `\varepsilon\in\{0,1\}`, mass `a\ge0`, and index `i\ge0`, such that

\[
\boxed{
\frac{c}{\mu(i+1+\mu)}
\le
G_{ii}^{(\varepsilon)}(a)
\le
\frac{C}{\mu(i+1+\mu)}.
}
\tag{1}
\]

The proof does not require a uniform Birkhoff--Adams expansion. It uses only the exact sign of the PF-247 Jacobi off-diagonals, the coefficient asymptotics and parity-independent `3/4` cancellation of [[research/prime_flute/findings/PF-262-massive-jacobi-resolvents-have-exact-double-root-indicial-law|PF-262]], and the exact spectral floor `L_\varepsilon\ge I` used in PF-265. The Jacobi quadratic form is a weighted one-dimensional Dirichlet energy with conductances comparable to `(j+1)^2` plus a bounded potential. A one-block trace/capacity argument then has exactly the scale `\mu(i+1)` when the mass length `(i+1)/\mu` contains several mode steps, and the trivial `\mu^2` scale when it does not.

As an immediate positive-resolvent Cauchy--Schwarz consequence,

\[
\boxed{
|G_{ij}^{(\varepsilon)}(a)|
\le
\frac{C}{\mu
\sqrt{(i+1+\mu)(j+1+\mu)}}.
}
\tag{2}
\]

Thus when `\mu\le i+1\le j+1`, PF-264's load-bearing `1/(\mu\sqrt{ij})` **mode amplitude is now uniform**, up to a fixed constant. When `\mu` dominates both indices, (2) automatically crosses to `O(\mu^{-2})`.

Equation (2) still does not multiply the sharp amplitude by PF-265's uniform ratio-decay exponent. What is now known uniformly is the joint envelope obtained by taking the minimum of the two independent estimates. The next question is therefore no longer whether the coupled mass/mode transition destroys the diagonal normalization. It is whether the amplitude and one-dimensional off-diagonal recession can be kept correlated strongly enough when summing PF-261's actual odd mass ladder.

## Claim

Let `L_\varepsilon` be either parity block of the exact PF-247 compactified-axis operator, written in parity-chain coordinates as

\[
(L_\varepsilon u)_j
=p_{j-1}^{(\varepsilon)}u_{j-1}
+q_j^{(\varepsilon)}u_j
+p_j^{(\varepsilon)}u_{j+1},
\qquad p_j^{(\varepsilon)}<0.
\tag{3}
\]

For `a\ge0` put

\[
T_{a,\varepsilon}=L_\varepsilon+a^2,
\qquad
\mu=\sqrt{1+a^2},
\qquad
G_{ij}^{(\varepsilon)}(a)
=\langle e_i,T_{a,\varepsilon}^{-1}e_j\rangle.
\tag{4}
\]

Then:

1. with
   \[
   c_j^{(\varepsilon)}:=-p_j^{(\varepsilon)}>0,
   \qquad
   V_j^{(\varepsilon)}
   :=q_j^{(\varepsilon)}-c_{j-1}^{(\varepsilon)}-c_j^{(\varepsilon)},
   \qquad c_{-1}^{(\varepsilon)}:=0,
   \tag{5}
   \]
   one has uniformly over the two parities
   \[
   c_j^{(\varepsilon)}\asymp(j+1)^2,
   \qquad
   V_j^{(\varepsilon)}=\frac34+O((j+1)^{-1});
   \tag{6}
   \]
2. consequently the Jacobi form satisfies, for finitely supported `u`,
   \[
   \langle u,L_\varepsilon u\rangle
   =\sum_{j\ge0}c_j^{(\varepsilon)}|u_{j+1}-u_j|^2
   +\sum_{j\ge0}V_j^{(\varepsilon)}|u_j|^2;
   \tag{7}
   \]
3. there is a parity-independent constant `C_0>0` such that
   \[
   \langle u,T_{a,\varepsilon}u\rangle
   \ge C_0\left[
   \sum_{j\ge0}(j+1)^2|u_{j+1}-u_j|^2
   +\mu^2\sum_{j\ge0}|u_j|^2
   \right];
   \tag{8}
   \]
4. the diagonal Green function obeys the two-sided estimate (1);
5. the full Green matrix obeys the amplitude estimate (2);
6. combining (2) with PF-265 gives the valid all-parameter envelope
   \[
   |G_{ij}^{(\varepsilon)}(a)|
   \le
   \min\left\{
   \frac{C}{\mu\sqrt{(i+1+\mu)(j+1+\mu)}},
   \frac4{\mu^2}e^{-\Phi_{ij}(\mu)}
   \right\},
   \tag{9}
   \]
   where
   \[
   \Phi_{ij}(\mu)
   :=\sum_{m=i}^{j-1}
   \min\left(1,\frac{c_p\mu}{m+1}\right)
   \qquad(i<j)
   \tag{10}
   \]
   is PF-265's uniform Jacobi metric.

No statement below claims that the minimum in (9) can be replaced by the product of the sharp amplitude and the full exponential factor.

## 1. The PF parity form has quadratic conductance and bounded potential

PF-247 gives `p_j^{(\varepsilon)}<0` exactly. PF-262 gives, with

\[
c_\varepsilon=\alpha+1+\varepsilon,
\]

\[
p_j^{(\varepsilon)}
=-j^2-c_\varepsilon j-d_\varepsilon+O(j^{-1}),
\tag{11}
\]

and

\[
q_j^{(\varepsilon)}
=2j^2+2(\alpha+\varepsilon)j+f_\varepsilon+O(j^{-1}),
\tag{12}
\]

together with the exact load-bearing cancellation

\[
c_\varepsilon-1-2d_\varepsilon+f_\varepsilon=\frac34.
\tag{13}
\]

Equation (11) and exact negativity imply

\[
0<c_-\le
\frac{c_j^{(\varepsilon)}}{(j+1)^2}
\le c_+<\infty
\tag{14}
\]

for both parities and all `j`: the ratio tends to `1`, and the finite prefix contains no zero off-diagonal coefficient.

Expanding `c_{j-1}` from (11),

\[
c_j+c_{j-1}
=2j^2+(2c_\varepsilon-2)j
+(1-c_\varepsilon+2d_\varepsilon)+O(j^{-1}).
\tag{15}
\]

Since `2c_\varepsilon-2=2(\alpha+\varepsilon)`, subtracting (15) from (12) and using (13) gives

\[
\boxed{
V_j^{(\varepsilon)}=\frac34+O(j^{-1}).
}
\tag{16}
\]

Thus `V_j` is bounded above and below uniformly over both fixed parities. Expanding the squares in

\[
\sum_j c_j|u_{j+1}-u_j|^2
\]

proves (7) first on finitely supported sequences and hence on the form core.

The `3/4` is not being used as an asserted global pointwise lower bound. Only boundedness of `V_j` is needed below; this avoids importing an unjustified finite-prefix positivity claim from its asymptotic limit.

## 2. Spectral positivity converts the form into a uniform weighted Sobolev norm

Let

\[
Q_{a,\varepsilon}[u]
:=\langle u,T_{a,\varepsilon}u\rangle.
\]

PF-265 uses the exact complete-axis realization to establish

\[
L_\varepsilon\ge I,
\]

so

\[
Q_{a,\varepsilon}[u]
\ge \mu^2\|u\|_2^2.
\tag{17}
\]

Let `C_V\ge0` satisfy `V_j^{(\varepsilon)}\ge-C_V` for all `j,\varepsilon`, and define

\[
E_\varepsilon[u]
:=\sum_j c_j^{(\varepsilon)}|u_{j+1}-u_j|^2.
\]

From (7),

\[
E_\varepsilon[u]
\le Q_{a,\varepsilon}[u]+C_V\|u\|_2^2
\le (1+C_V)Q_{a,\varepsilon}[u],
\tag{18}
\]

where `\mu\ge1` was used in the second step. Combining (14), (17), and (18), then taking half the sum of the two resulting lower bounds, gives (8) for a fixed positive constant `C_0` independent of `a`, `u`, and parity.

This is the point at which the exact spectral floor matters. The asymptotic `V_j\to3/4` alone would not justify discarding a potentially negative finite prefix from the form.

## 3. A local trace inequality proves the uniform upper Green amplitude

For a positive self-adjoint `T_{a,\varepsilon}`, the diagonal resolvent has the variational representation

\[
G_{ii}^{(\varepsilon)}(a)
=
\sup_{u\ne0}
\frac{|u_i|^2}{Q_{a,\varepsilon}[u]}.
\tag{19}
\]

If `\mu\ge i+1`, (17) gives directly

\[
Q_{a,\varepsilon}[u]
\ge\mu^2|u_i|^2
\ge\frac12\mu(i+1+\mu)|u_i|^2.
\tag{20}
\]

Now assume `1\le\mu<i+1` and put

\[
M=\left\lfloor\frac{i+1}{\mu}\right\rfloor\ge1.
\tag{21}
\]

For every `0\le r\le M`, telescoping from `i` to `i+r` and Cauchy--Schwarz give

\[
|u_i|^2
\le2|u_{i+r}|^2
+2M\sum_{k=i}^{i+M-1}|u_{k+1}-u_k|^2.
\]

Averaging over `r=0,\dots,M` yields

\[
|u_i|^2
\le
\frac{2}{M+1}\sum_{r=0}^M|u_{i+r}|^2
+2M\sum_{k=i}^{i+M-1}|u_{k+1}-u_k|^2.
\tag{22}
\]

Because `M+1>(i+1)/\mu`, `M\le(i+1)/\mu`, and `(k+1)^2\ge(i+1)^2` on the displayed edge interval, multiplying (22) by `\mu(i+1)` gives

\[
\mu(i+1)|u_i|^2
\le
2\mu^2\|u\|_2^2
+2\sum_{k\ge0}(k+1)^2|u_{k+1}-u_k|^2.
\tag{23}
\]

Equation (8) therefore implies

\[
Q_{a,\varepsilon}[u]
\gtrsim \mu(i+1)|u_i|^2.
\]

Since `\mu<i+1`, `\mu(i+1+\mu)\le2\mu(i+1)`. Together with (20) and (19), this proves the upper half of (1).

The scale `(i+1)/\mu` is not inserted by analogy: it is the block length at which the weighted gradient cost `(i+1)^2/M` and the mass cost `\mu^2M` balance.

## 4. A matching tent function proves that the diagonal scale is sharp

The same coefficient information gives the reverse inequality. From (6), there is a fixed `C_1` such that on finitely supported sequences

\[
Q_{a,\varepsilon}[u]
\le C_1\left[
\sum_j(j+1)^2|u_{j+1}-u_j|^2
+\mu^2\sum_j|u_j|^2
\right].
\tag{24}
\]

Indeed `c_j\lesssim(j+1)^2`, `V_j` is bounded above, and `a^2+O(1)\lesssim\mu^2`.

If `\mu\ge(i+1)/2`, use the point mass `u=e_i`. Since `q_i\lesssim(i+1)^2`,

\[
Q_{a,\varepsilon}[e_i]
=q_i+a^2
\lesssim\mu^2
\lesssim\mu(i+1+\mu).
\tag{25}
\]

If `1\le\mu<(i+1)/2`, put

\[
M=\left\lfloor\frac{i+1}{2\mu}\right\rfloor\ge1
\]

and choose the symmetric discrete tent centered at `i`, equal to `1` at `i`, decreasing linearly with slope `1/(M+1)` on both sides, and equal to zero outside distance `M+1`. This support stays in the half-line because `M+1\le i+1` in the present regime. On its support `j+1\asymp i+1`, so

\[
\sum_j(j+1)^2|u_{j+1}-u_j|^2
\lesssim \frac{(i+1)^2}{M+1}
\lesssim \mu(i+1),
\tag{26}
\]

while

\[
\mu^2\sum_j|u_j|^2
\lesssim\mu^2(M+1)
\lesssim\mu(i+1).
\tag{27}
\]

Equations (24), (26), and (27) produce a test function with `u_i=1` and

\[
Q_{a,\varepsilon}[u]
\lesssim\mu(i+1+\mu).
\tag{28}
\]

The reciprocal Dirichlet principle corresponding to (19) therefore gives the lower half of (1). In particular there is **no hidden diagonal transition regime** in which the fixed-mass `1/(\mu i)` normalization blows up before crossing to the large-mass `\mu^{-2}` scale.

## 5. The sharp amplitude is uniform off diagonal, but not yet multiplicatively correlated with decay

Because `T_{a,\varepsilon}^{-1}` is positive,

\[
|G_{ij}|^2
\le G_{ii}G_{jj}
\tag{29}
\]

by Cauchy--Schwarz in the positive-resolvent semi-inner product. Substitution of (1) proves (2).

This already covers all coupled regimes with the correct endpoint interpolation. In particular, if `\mu\le i+1\le j+1`,

\[
|G_{ij}^{(\varepsilon)}(a)|
\lesssim\frac1{\mu\sqrt{(i+1)(j+1)}},
\tag{30}
\]

which is the amplitude factor missing from PF-265. If `i+1\le j+1\le\mu`, (2) is `O(\mu^{-2})`.

However (29) does not carry PF-265's distance factor. The two proven bounds can only be combined for free as the minimum (9), or by interpolation. For every `0\le\vartheta\le1`, for example,

\[
|G_{ij}|
\lesssim_\vartheta
\mu^{-2+\vartheta}
[(i+1+\mu)(j+1+\mu)]^{-\vartheta/2}
\exp[-(1-\vartheta)\Phi_{ij}(\mu)].
\tag{31}
\]

This spends a fraction of the sharp amplitude when it retains a fraction of the Combes--Thomas exponent. It must not be advertised as PF-264's full prefactor times PF-265's full decay.

The structurally clean remaining theorem is therefore a **normalized Green-correlation estimate** such as

\[
\boxed{
\frac{|G_{ij}^{(\varepsilon)}(a)|}
{\sqrt{G_{ii}^{(\varepsilon)}(a)G_{jj}^{(\varepsilon)}(a)}}
\lesssim
\exp[-c\Phi_{ij}(\mu)]
}
\tag{32}
\]

with a fixed `c>0`. Combining (32) with (1) would give the desired uniform sharp amplitude and off-diagonal recession simultaneously. Alternatively, the minimum envelope (9) may already suffice after the **actual** odd-mass sum; that should be tested before proving a stronger theorem than needed.

## 6. Prior-art and novelty audit

No novelty is claimed for the variational formula (19), the one-dimensional trace/tent argument, positive-resolvent Cauchy--Schwarz, or the general principle that weighted Dirichlet forms control Green diagonals. These are standard functional-analytic/potential-theoretic tools.

The closest already-used Green-matrix prior art remains J. Janas, S. Naboko, and L. O. Silva, *Green matrix estimates of block Jacobi matrices I: Unbounded gap in the essential spectrum*, Integral Equations and Operator Theory **90** (2018), Paper 49, DOI `10.1007/s00020-018-2476-0`, arXiv:1801.01924. PF-265 specializes that theorem to obtain the mass-uniform decay metric, but its usable all-mass prefactor is `O(\mu^{-2})`, not the mode-sensitive diagonal scale (1).

A targeted search also found the broad weighted discrete-Hardy literature, for example M. Sh. Braverman and V. D. Stepanov, *On the Discrete Hardy Inequality*, Bulletin of the London Mathematical Society **26** (1994), 283--287, DOI `10.1112/blms/26.3.283`. That literature confirms that one-dimensional weighted trace/Hardy mechanisms are classical; it is not imported as a theorem here because (22)--(28) are elementary and proved directly.

The project-specific content is the observation that PF-262's exact parity coefficients reduce the massive Prime-Flute Green diagonal to the balanced weighted scale in (1), uniformly across the same coupled `a,i` regime left open by PF-264/PF-265. A targeted search did not identify an already packaged theorem with this exact `\mu(i+\mu)` specialization for the PF operator. The claim should therefore be read as an exact derived specialization, not as a new general theorem on Jacobi matrices.

## 7. Boundaries and adversarial checks

1. **No pointwise claim `V_j\ge3/4`.** Only `V_j=3/4+O(j^{-1})` and global boundedness are used. Finite-prefix signs are absorbed through the exact spectral floor `L_\varepsilon\ge I`.
2. **The spectral floor is essential.** Without `L_\varepsilon\ge I`, bounded-below `V_j` would not by itself imply the uniform form lower bound (8) when `a` is small.
3. **All mode indices are covered.** The constants absorb the finite prefix because `c_j/(j+1)^2` is positive at every finite index and tends to `1`.
4. **The lower bound is a scale check, not positivity folklore.** The tent function is supported on a block of length `\asymp(i+1)/\mu` only when that block fits; otherwise the point-mass test gives the correct `\mu^{-2}` regime.
5. **Cauchy--Schwarz does not create distance decay.** Equation (2) is a uniform amplitude theorem only. Multiplying it by PF-265's exponential without a new argument would be invalid.
6. **The minimum envelope is rigorous.** Equation (9) uses two independently valid upper bounds and therefore needs no correlation assumption.
7. **No odd-ladder/operator-norm conclusion.** The full PF-261 mass sum, endpoint-weighted `R>1` norm, combined PF-257 Robin transform, PF-256 actual-corridor transfer, PF-243 reassembly, scattering/determinants, zeta zeros, and RH remain open.

The finding would fail if PF-247 had a vanishing/off-sign parity coupling, if PF-262's quadratic coefficient scale or `3/4` cancellation were wrong, or if the parity realization did not satisfy the exact spectral floor used in PF-265. Those inputs are already persisted independently.

## Decisive next test

Do **not** spend another cycle trying to establish the diagonal interpolation: (1) closes it. Start by inserting the rigorous joint envelope (9) into PF-261's actual odd mass sum

\[
a_k=\frac{(2k+1)\pi}{2rs}
\]

and split the low/intermediate/high mass ranges only where the minimum changes branch. Determine whether the summed kernel already retains a strict separated `R>1` window after PF-261's outer `A^{-1/4}` weights.

If the minimum loses exactly the critical power, attack the normalized correlation estimate (32), or an equivalent one-dimensional transfer/Weyl estimate that preserves the diagonal capacities while adding a fixed positive fraction of PF-265's metric. Such a theorem would combine PF-266's now-uniform amplitude with PF-265's now-uniform recession without hiding either effect in a mass-dependent connection coefficient. Only after the **summed** fixed-axis bound survives should the argument be propagated through the combined Robin transform and then through the actual corridor/hypercycle geometry.