# PF-353 — complete common-frequency fibres retain the coupled corridor angle

**Status:** EXACT-DERIVED + CLASSICAL-DISPLACEMENT-METHODS + COUPLED-CORRIDOR-MODEL-OBSTRUCTION + ACTUAL-PRIME-FLUTE-ANGLE-OPEN.

PF-352's complete-lattice control cancels one retained pair, but its **full retained low/high angle cannot tend to zero**. On both modules, retain the constant Fourier mode and the physical frequency `2`. These are admissible common low and high frequencies for every member of that family. After eliminating both complete transition bands, the two canonical correlations between these two-dimensional frequency spaces are exactly

\[
\boxed{\rho_*=
\frac{2\sqrt{\cosh(2\pi)}}{1+\cosh(2\pi)}
=0.121772401\ldots.}
\tag{1}
\]

This holds at every strictly positive grounding, including the grounding roots that cancel PF-352's original pair. The proof is a finite matrix identity: positive Cauchy displacement structure survives arbitrary mismatched transition elimination, and a complete common-frequency space has exactly the dimension needed to normalize away the surviving generator matrices.

This closes the whole-angle-decay interpretation of that particular corridor-model family. It does not invalidate its zero-entry result, identify the model with the pant DtN form, or establish noncompactness for the actual prime flute.

## 1. Finite positive network with unequal frequency sets

Let `K` be a real symmetric strictly positive `d by d` matrix. For each module `i`, choose a finite set of distinct positive Cauchy nodes `x`. Nodes may coincide on different modules. For the resulting labels `(i,x)`, define

\[
 M_{(i,x),(j,y)}=\frac{K_{ij}}{x+y}.
\tag{2}
\]

This is the coefficient form of the network energy

\[
 E(f_1,\ldots,f_d)=\sum_{i,j}K_{ij}\langle f_i,f_j\rangle,
 \qquad f_i=\sum_x z_{i,x}k_x,
 \quad \langle k_x,k_y\rangle=(x+y)^{-1}.
\tag{3}
\]

It includes grounded nearest-neighbor difference energies; no sign assumption on individual entries of `K` is needed. Strict positivity follows directly from

\[
 z^{\mathsf T}Mz=\int_0^\infty v(r)^{\mathsf T}Kv(r)\,dr,
 \qquad v_i(r)=\sum_x z_{i,x}e^{-xr}.
\tag{4}
\]

A zero integral forces every `v_i` to vanish. Distinct exponentials on each module are linearly independent, so every coefficient vanishes.

Partition the labels into retained `X` and transition `T`, and let

\[
 S=M^{/T}=M_{XX}-M_{XT}M_{TT}^{-1}M_{TX}>0.
\tag{5}
\]

There is no restriction on the size or agreement of the transition sets. Fix `0<a<b`, and suppose the retained set includes **every** module label at both nodes:

\[
 F_a=\{(i,a):1\le i\le d\},\qquad
 F_b=\{(i,b):1\le i\le d\}.
\tag{6}
\]

A complete frequency fibre means precisely one of these `d`-dimensional coefficient spaces. Other retained labels may be present. The following statements concern principal blocks of the same shorted form (5), without eliminating those other retained labels.

Write `A=S_(F_a,F_a)`, `B=S_(F_b,F_b)`, and `C=S_(F_a,F_b)`. Then

\[
\boxed{
 C B^{-1}C^{\mathsf T}=\frac{4ab}{(a+b)^2}A,
 \qquad
 \sigma_j(A^{-1/2}CB^{-1/2})=\frac{2\sqrt{ab}}{a+b}
 \quad(1\le j\le d).
}
\tag{7}
\]

Thus arbitrary intermodule transition mismatch can rotate the surviving coupled directions, but cannot change their complete-fibre canonical correlations.

## 2. Positive displacement identity and proof

Let `D` be diagonal with the node `x` in coordinate `(i,x)`, and let the corresponding row of `V` be `e_i^T`. Equation (2) gives

\[
 DM+MD=VKV^{\mathsf T}.
\tag{8}
\]

Put `R=M_TT^(-1)` and

\[
 H=V_X-M_{XT}R V_T.
\tag{9}
\]

Then the exact Schur displacement identity is

\[
\boxed{D_XS+SD_X=HKH^{\mathsf T}.}
\tag{10}
\]

For completeness, use the three blocks of (8):

\[
 D_XM_{XX}+M_{XX}D_X=V_XKV_X^{\mathsf T},
\]
\[
 D_XM_{XT}+M_{XT}D_T=V_XKV_T^{\mathsf T},
 \qquad
 D_TM_{TT}+M_{TT}D_T=V_TKV_T^{\mathsf T}.
\]

Inserting (5), the two mixed subtractions produce
`-V_X K V_T^T R M_TX` and its transpose, together with
`M_XT(D_T R+R D_T)M_TX`. Multiplying the last displayed block identity on both sides by `R` identifies this last term as
`M_XT R V_T K V_T^T R M_TX`. This is exactly the expansion of (10). Empty `T` gives (10) with `H=V`.

Let `H_a,H_b` be the `d by d` row restrictions in (9). Since `D` is scalar on each complete fibre, (10) implies

\[
 A=\frac{H_a K H_a^{\mathsf T}}{2a},\qquad
 B=\frac{H_b K H_b^{\mathsf T}}{2b},\qquad
 C=\frac{H_a K H_b^{\mathsf T}}{a+b}.
\tag{11}
\]

Both `A` and `B` are strictly positive. Therefore `H_a,H_b` are invertible. Substitution into `CB^(-1)C^T` proves (7), since

\[
 K H_b^{\mathsf T}(H_b K H_b^{\mathsf T})^{-1}H_b K=K.
\tag{12}
\]

Equivalently, `A^(-1/2)H_a K^(1/2)/sqrt(2a)` and its `b` analogue are orthogonal matrices. The normalized mixed block is their product times `2sqrt(ab)/(a+b)`. Scalar entry cancellation is compatible with nontrivial orthogonal mixing of the module directions.

## 3. The witness survives enlargement of the retained low/high spaces

Suppose `F_a` lies in the retained low space `L` and `F_b` in the retained high space `Hh`. To avoid confusing the high space with the generator in (9), write the full angle as

\[
 Z=S_{LL}^{-1/2}S_{L,Hh}S_{Hh,Hh}^{-1/2}.
\]

Let `J_a,J_b` insert the complete fibres into those coefficient spaces. The matrices

\[
 U_a=S_{LL}^{1/2}J_a A^{-1/2},\qquad
 U_b=S_{Hh,Hh}^{1/2}J_b B^{-1/2}
\]

are isometries, because `J_a^T S_LL J_a=A` and likewise for `B`. Moreover,

\[
 U_a^{\mathsf T} ZU_b=A^{-1/2}CB^{-1/2}.
\tag{13}
\]

The singular-value min-max principle, or contraction of approximation numbers under isometric compression, now gives

\[
\boxed{\sigma_j(Z)\ge\frac{2\sqrt{ab}}{a+b},\qquad 1\le j\le d.}
\tag{14}
\]

The normalization here uses the diagonal blocks of the **same globally shorted finite form**. It is not an entrywise normalization in the original unshorted coefficient metric. Extra retained modes can be included without weakening (14); further elimination of retained modes is a different operation.

## 4. Apply the identity to PF-352's complete Fourier lattices

That family has a fixed transition interval `(1,1+1/M)` with sufficiently large fixed integer `M`, and

\[
 N=M(2j+2),\qquad L_1=2\pi(N-\tfrac12),\qquad L_2=2\pi N.
\tag{15}
\]

Each module eliminates every Fourier mode in the open transition band. Restore the following exterior modes as retained variables on **both** modules:

\[
 \xi_{\rm low}=0,\qquad \xi_{\rm high}=2.
\tag{16}
\]

Frequency `2` has integer Fourier indices `2N-1` and `2N` on the respective modules; the zero modes are their constants. Both frequencies are outside the transition band and lie in the intended low and high sectors. Thus this witness uses exact sampled lattice modes, not continuum interpolation or omitted transition frequencies.

The cosine/Cauchy identification of PF-346 extends to `x=1`:

\[
 k_x(t)=\frac{\cos(\pi^{-1}\operatorname{arcosh}(x)t)}{\sqrt{\pi(x+1)}},
 \qquad x\ge1,
 \qquad \langle k_x,k_y\rangle_{L^2(\operatorname{sech}t\,dt)}
 =\frac1{x+y}.
\tag{17}
\]

At `x=1`, this is the ordinary constant cosine, with positive squared norm `1/2`. It has no relation to the degenerate prime endpoint `p=2` in the flute construction. Here `x` is a frequency parameter, not a sampled prime or endpoint.

For the energy in PF-352, take

\[
 K=c_1\begin{pmatrix}1+\tau&-1\\-1&1+\tau\end{pmatrix}>0,
 \qquad c_1>0,\quad\tau>0.
\tag{18}
\]

Its eigenvalues are `c_1 tau` and `c_1(2+tau)`. Apply (7) with `d=2`, `a=1` and `b=cosh(2pi)` to obtain (1). Apply (14) to obtain two uniformly positive singular values of every enlarged retained low/high finite-section angle.

This holds in particular at every `tau_* in (0,1)` supplied by PF-352. Restoring additional **retained** variables leaves the original pair's principal shorted block unchanged: its entries in (5) depend only on that pair and `T`. Its zero mixed entry therefore coexists with the two nonzero block correlations (1). The complete low/high model angle does not decay along the growing-lattice family even though the original pair correlation is exactly zero.

Including all sine transition modes makes no difference to this cosine witness: cosine/sine inner products vanish against the even corridor weight, also across modules. Positive physical Fourier normalization is an invertible block-preserving diagonal congruence and leaves canonical correlations unchanged. Actual seam face-parity variables are not part of the corridor model.

## Prior art, verification, and evidence boundary

The displacement recursion is classical. Gohberg, Kailath and Olshevsky, *Fast Gaussian Elimination with Partial Pivoting for Matrices with Displacement Structure* (1995), [Lemma 1.1 and equations (1.3)–(1.4)](https://www2.math.uconn.edu/~olshevsky/papers/geppdsam.pdf), preserve Cauchy-like generators through Schur elimination. Equations (8)–(10) are its positive symmetric block specialization, proved directly here. Forrester and Zhang, *Parametrising correlation matrices* (2020), [equations (2.6)–(2.7)](https://arxiv.org/abs/1812.07685), give the standard Schur/partial-correlation context. Grounded network elimination is classical Kron reduction as in Dörfler and Bullo, [*Kron Reduction of Graphs With Applications to Electrical Networks*](https://motion.me.ucsb.edu/pdf/2011d-db.pdf). These sources are already S23/S28.

No new general displacement theorem or general theory of canonical correlations is claimed. The line-specific addition is the **complete retained frequency-space invariant under mismatched elimination**, and its exact use of PF-352's common frequencies to rule out whole-angle decay in a family that cancels an individual pair. This is not PF-351's common-transition tensor argument: the eliminated labels here may be entirely different on the modules.

Supplementary Python standard-library `Fraction` checks used `d=2,3`, the path-graph Laplacian plus `tau I` for `tau in {1,1/7,1/1000}`, retained nodes `a=1,b=6`, and transition sets `{(5+i)/2,(7+i)/2}` for zero-based module index `i`, either unchanged or with `9/2` added (`19/4` instead if `9/2` was already present). This includes overlaps between modules. All 12 cases had positive elimination pivots and satisfied (7) and (10) exactly. A separate check used PF-351's rational data `a=2,b=5`, transition nodes `3` and `4`, and grounds `1/2646,1/2647`. After restoring both complete fibres, the original module-1 mixed entry was still exactly zero, while (7) gave **both squared block correlations `40/49`**. The general conclusions follow from the identities above, not from these finite checks.

The limitations are substantive:

- `K>0` is essential for the stated invertible normalization. No uniform lower eigenvalue bound is required, but `tau=0` in (18) is excluded. Sending `tau` to zero through positive values preserves the finite identities; substituting zero can destroy positivity when full fibres are retained.
- Both retained frequencies must be present on **every** module participating in `K`. Merely close frequencies do not meet (6); a stability estimate at the shorted diagonal scale would be needed. Arbitrary prime-flute cuff periods are not shown to have a common bounded nonzero Fourier frequency.
- The result controls exact finite corridor forms. It does not justify their replacement by the full pant/seam energy, attachment to more modules without checking complete fibres, or an infinite-section operator limit.
- Two persistent singular values in each finite model rule out angle-norm decay along this family. They do not by themselves prove noncompactness of one infinite prime-flute operator, or any weak trace, scattering, zeta-zero or RH statement.

The remaining actual-surface question still needs the unequal physical cuff lattices and the pant/seam remainder controlled after normalization. PF-352's single-pair cancellation remains a valid warning against transferring a local scalar witness. It is not a model construction in which the whole retained low/high angle disappears: complete common-frequency directions furnish the explicit obstruction (1).
