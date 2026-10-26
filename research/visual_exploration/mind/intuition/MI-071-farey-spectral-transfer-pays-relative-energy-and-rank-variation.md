# MI-071 — Farey spectral transfer pays relative energy and rank variation separately

**Evidence level:** supported by the exact normalized-spectrum inequality of [VIS-447](../../findings/VIS-447-uniform-normalized-farey-transport-spectrum.md), the capped variation bound of [VIS-465](../../findings/VIS-465-capped-variation-tariff-for-farey-transport-spectrum.md), and the stitch-parity identities of [VIS-466](../../findings/VIS-466-reflected-farey-transport-parity-is-a-stitch-boundary-term.md), applied to [FD-320](../../../farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md). These are classical finite-dimensional/Fourier mechanisms specialized to labeled excursion controls, not new arithmetic cancellation.

Fix a prime `p>=7`, `N=N_p=sum_(q<=p) phi(q)`, and a whole-excursion permutation `sigma`. The genuine Farey discrepancy `D` and reassembled discrepancy `y` obey

`y=P_sigma D+v`, `E=||D||_2^2=o(1)`, `T=||v||_2^2`.

Assume `T>0` and `y!=0`. For the orthonormal Dirichlet sine transform, put `pi_m(z)=|zhat_m|^2/||z||_2^2` and `F_J(z)=sum_(m in J) pi_m(z)`. The absolute vector error transports **every** normalized mode subset with no dimension loss:

`sup_J |F_J(y)-F_J(v)| = (1/2) sum_m |pi_m(y)-pi_m(v)| <= min(1,sqrt(E/T))`.

The denominator is essential: `E=o(1)` and `T=o(1)` alone do not identify the normalized spectrum. For a fixed comparator with its own expected fraction `f_null(J)>0`, the error in `S_J=F_J/f_null(J)` is at most `min(1,sqrt(E/T))/f_null(J)`. Thus even `E=o(T)` may be insufficient for a vanishing null fraction; `sqrt(E/T)=o(f_null(J))` suffices.

Extend `v` by `v_0=v_N=0`. Set

`V=sum_(j=1)^N |v_j-v_(j-1)|`, `R=N V^2/T`,

`B_q=V^2/(2NT) sum_(m=q+1)^(N-1) csc^2(pi m/(2N))`, `1<=q<N`.

Abel summation gives the tail majorant and Parseval gives its independent probability cap:

`1-F_{1,...,q}(v) <= min(1,B_q) <= min(1,R/(2q))`.

The cap applies to the bound on the tail; the uncapped majorant can exceed one. For `N=3`, `v=(1,-1)`, `q=1`, the tail is one while `B_q=16/9`. Combining the two mechanisms yields

`1-F_{1,...,q}(y) <= min(1,R/(2q)) + min(1,sqrt(E/T))`.

In particular `E/T->0` and `R=o(q_p)` suffice for low-band share tending to one. Conversely, if that share is at most `1-eta` and `sqrt(E/T)<eta`, then `R>=2q(eta-sqrt(E/T))`. Large roughness is necessary for transport-dominated depletion; it is not sufficient.

The roughness is computable without the within-excursion grid. With positive gap counts `ell_j`, `w_j=ell_j/N-1/p`, `U_j=sum_(i<j)w_i`, and `c_t=U_(sigma(t))-sum_(s<t)w_(sigma(s))`,

`T=sum_(t=1)^(p-2) ell_(sigma(t)) c_t^2`,

`V=|c_1|+sum_(t=1)^(p-3)|c_(t+1)-c_t|+|c_(p-2)|`.

Thus the controlling quantity is the size of cumulative displacement jumps relative to their weighted energy, not the count or near-integrality of Hall–Shiu defects. In VIS-465's reflected four-defect control, `R->16` and `T->3/(4pi^2)>0`, so every divergent full-mode cutoff captures asymptotically all normalized energy.

Reflection must be imposed on the correct vector. Under `sigma(n+1-t)=p-1-sigma(t)`, `n=p-2`, the full `y` is rank-antisymmetric, but FD-320's **right-endpoint transport** generally is not. With `r_t=1+sum_(u<=t) ell_(sigma(u))`, `r_0=1`, `r_n=N-1`, `c_0=c_(n+1)=0`, and `(Jz)_k=z_(N-k)`, VIS-466 gives

`s=(v+Jv)/2`, `a=(v-Jv)/2`, `s_(r_t)=(c_t-c_(t+1))/2`, with `s=0` off the stitches,

`L=||s||^2=sum_(m odd)|vhat_m|^2=(1/4)sum_(t=0)^n(c_(t+1)-c_t)^2 <= E`,

`||a||^2=T-L`, `||y-a||^2=E-L`.

For `T>0`, `0<L<T`. The symmetric part of `P_sigma D` equals `-s` and cancels the raw transport's odd modes exactly. Thus FD-320 §3's assertion of odd-mode vanishing in the all-mode identity is valid for `y`, but cannot be assigned separately to its two summands. Its vector identity and absolute error remain intact.

On the same full mode index set, `TV(pi(v),pi(a))=L/T` and `TV(pi(y),pi(a))<=min(1,sqrt((E-L)/(T-L)))`. Projection removes the known stitch artifact and never worsens the capped sufficient transfer bound, but does not control the remaining even-sector error or a null fraction denominator. The four-defect family has `L=1/(4p^2)` and `L/T=1/(N-4)`: leakage vanishes asymptotically but is nonzero at every finite order.

The first `q` even modes equal the full cutoff `2q` for `y` and `a`, **not for raw `v`**. Applying the original full-band bound at `2q<N` still gives `R/(4q)` in the tail estimate for `y`, with its original `sqrt(E/T)` error. Unreflected controls require the full basis; a projected transport is an analysis vector, not another admissible reassembled grid.

[VIS-467](../../findings/VIS-467-vanishing-stitch-parity-dominates-farey-high-bands.md) shows that the vanishing global leakage is **leading-order inside a fixed high band**. In the four-defect family, `N` is even, `b=1/(2p)`, and raw `v_k` equals `b` on `2<=k<=N/2-1`, `-b` on `N/2+2<=k<=N-1`, and zero elsewhere. For fixed `0<alpha<1`, let `B=B_alpha={m:alpha<=m/N<1}` and let `pi^B` normalize by energy inside `B`. Separate sine sums in the four mode residue classes give weak limits of finite intensity measures, with `delta_x` the point mass at `x`:

`N sum_(m in B_alpha, odd) pi_m(v) delta_(m/N) -> dx`,

`N sum_(m in B_alpha, even) pi_m(v) delta_(m/N) -> g(x) dx`, `g(x)=2 cos^2(pi x) cot^2(pi x/2)` on `[alpha,1]`.

Put `M(alpha)=1-alpha+int_alpha^1 g(x) dx`. For sufficiently large `N` both band energies are positive. Since `a` keeps precisely the even coefficients of `v`, disjoint parity support gives

`TV(pi^B(v),pi^B(a))=pi^B(v)(odd) -> (1-alpha)/M(alpha)`.

At `alpha=1/2` this is `pi/(16-4pi)=0.914948...`, although globally the distance is only `1/(N-4)`. For the full reassembled `y`, exact antisymmetry gives `TV(pi^B(y),pi^B(v))>=pi^B(v)(odd)` whenever its band law exists. This is a lower bound, not an identification of the even spectra of `y` and `a`. The band energies are `||Pi_B v||^2 ~ b^2 M(alpha)` and `||Pi_B s||^2 ~ b^2(1-alpha)`: both are of order `p^(-2)`, while `T` is of order one.

After the stitch projection, the sufficient transfer condition from [VIS-450](../../findings/VIS-450-projected-parity-transfer-sharpens-farey-gate.md) is instead `||Pi_B Q_- P_sigma D||^2 / ||Pi_B a||^2 -> 0`, where `Q_-=(I-J)/2` uses the rank-reversal operator defined above. The global corrected ratio `(E-L)/(T-L)` cannot replace this band ratio. All high-band limits keep `alpha` fixed before `N->infinity`; they give no uniform shrinking-band limit. This realizes the conditioning obstruction within the actual excursion control, without asserting an anomaly of the genuine Farey spectrum.

This is a one-sided criterion on artificial labeled-edge reassemblies. Genuine Farey order has `T=0`, outside the normalized transport comparison. Neither exact recovery of a reassembly nor bounded transport roughness proves suppression in the genuine Farey spectrum; a source-natural comparator still needs its own band normalization.
